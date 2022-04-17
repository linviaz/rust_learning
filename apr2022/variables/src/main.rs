fn main() {
    let x = 5;
   // println!("The value of x is: {}", x);
    //x = 6;
    //println!("The value of x is: {}", x);

    //const THREE_HOURS_IN_SECONDS: u32 = 60*60*3;
    //println!("3 hours in seconds are: {}.", THREE_HOURS_IN_SECONDS);
    let x = x + 1;

    {
        let x = x * 2;
        println!("The value of x in the inner scope is: {}", x);
    }

    println!("The value of x is: {}", x);

    let spaces = "         ";
    let spaces = spaces.len();

    println!("len of spaces: {}", spaces);
    // let mut spaces = "      ";
    // spaces = spaces.len();
    // // The above code won't run with a compiler-time error of mutating a variable's type.
}
