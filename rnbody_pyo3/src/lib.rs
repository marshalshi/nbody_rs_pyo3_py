use pyo3::prelude::*;
use pyo3::wrap_pyfunction;


#[pyclass]
#[derive(Clone, Copy, Debug)]
pub struct Planet {
    x: f64, y: f64, z: f64,
    vx: f64, vy: f64, vz: f64,
    mass: f64,
}
#[pymethods]
impl Planet {
    #[new]
    fn new(x: f64, y: f64, z: f64, vx: f64, vy: f64, vz: f64, mass: f64) -> Self {
        Planet { x, y, z, vx, vy, vz, mass }
    }
}

#[pyfunction]
pub fn advance_planet_struct(bodies: Vec<Planet>, dt: f64, steps: i32) -> Vec<Vec<f64>> {
    let mut bodies = bodies;
    for _ in 0..steps {
        let mut b_slice: &mut [Planet] = &mut bodies;
        loop {
            let bi = match shift_mut_ref(&mut b_slice) {
                Some(bi) => bi,
                None => break
            };
            for bj in b_slice.iter_mut() {
                let dx = bi.x - bj.x;
                let dy = bi.y - bj.y;
                let dz = bi.z - bj.z;

                let d2 = dx * dx + dy * dy + dz * dz;
                let mag = dt / (d2 * d2.sqrt());

                let massj_mag = bj.mass * mag;
                bi.vx -= dx * massj_mag;
                bi.vy -= dy * massj_mag;
                bi.vz -= dz * massj_mag;

                let massi_mag = bi.mass * mag;
                bj.vx += dx * massi_mag;
                bj.vy += dy * massi_mag;
                bj.vz += dz * massi_mag;
            }
            bi.x += dt * bi.vx;
            bi.y += dt * bi.vy;
            bi.z += dt * bi.vz;
        }
    }
    let mut res = Vec::with_capacity(bodies.len());
    for b in bodies {
        res.push(vec![b.x, b.y, b.z, b.vx, b.vy, b.vz, b.mass]);
    }
    res
}

#[pyfunction]
pub fn advance_list(bodies: Vec<Vec<f64>>, dt: f64, steps: i32) -> Vec<Vec<f64>>{
    let mut bodies = bodies;
    for _ in 0..steps {
        let mut b_slice: &mut [Vec<f64>] = &mut bodies[..];
        loop {
            let bi = match shift_mut_ref(&mut b_slice) {
                Some(bi) => bi,
                None => break
            };
            for bj in b_slice.iter_mut() {
                let dx = bi[0] - bj[0];
                let dy = bi[1] - bj[1];
                let dz = bi[2] - bj[2];

                let d2 = dx * dx + dy * dy + dz * dz;
                let mag = dt / (d2 * d2.sqrt());

                let massj_mag = bj[6] * mag;
                bi[3] -= dx * massj_mag;
                bi[4] -= dy * massj_mag;
                bi[5] -= dz * massj_mag;

                let massi_mag = bi[6] * mag;
                bj[3] += dx * massi_mag;
                bj[4] += dy * massi_mag;
                bj[5] += dz * massi_mag;
            }
            bi[0] += dt * bi[3];
            bi[1] += dt * bi[4];
            bi[2] += dt * bi[5];
        }
    }

    bodies
}


#[pymodule]
fn rnbody_pyo3(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(advance_planet_struct))?;
    m.add_wrapped(wrap_pyfunction!(advance_list))?;
    m.add_class::<Planet>()?;
    Ok(())
}


/// Pop a mutable reference off the head of a slice, mutating the slice to no
/// longer contain the mutable reference.
fn shift_mut_ref<'a, T>(r: &mut &'a mut [T]) -> Option<&'a mut T> {
    if r.len() == 0 { return None }
    let tmp = std::mem::replace(r, &mut []);
    let (h, t) = tmp.split_at_mut(1);
    *r = t;
    Some(&mut h[0])
}
