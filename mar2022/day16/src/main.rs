extern crate rand;

use rand::Rng;

fn montecarlo_pi(trials: u32) -> f64 {
    let mut count: u32 = 0;

    //each thread has an initialized generator
    //floating numbers are uniformly distributed from 0 up to but not including 1
    let mut rng = rand::thread_rng();

    for _i in 1..trials {
        let x: f64 = rng.gen::<f64>();
        let y: f64 = rng.gen::<f64>();
        let p: f64 = x.powf(2.0) + y.powf(2.0);

        if p < 1.0 {
            count += 1;
        }
    }

    let pi_estm: f64 = (count as f64)*4.0/(trials as f64);
    return pi_estm
}


fn main() {
    let pi_eval: f64 = montecarlo_pi(1000000);

    println!("[1] {pi}", pi = pi_eval);
}
