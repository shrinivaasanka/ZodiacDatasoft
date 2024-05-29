fn main()
{
    let buyer1 = 10;
    let seller1 = buyer1;
    println!("Before buying - buyer1 has {} Neuros",buyer1);
    println!("Seller1 receives {} Neuros",seller1);
    println!("Copy of Neuro cryptocurrency - After buying - buyer1 has {} Neuros",buyer1);
    let buyer2 = String::from("ff20a894-a2c4-4002-ac39-93d053ea3020:100");
    println!("Before buying - buyer2 has {} Neuros",buyer2);
    let seller2 = buyer2;
    println!("Move of Neuro cryptocurrency - Seller2 receives {}",seller2);
    //println!("This won't compile - After buying - buyer2 has {}",buyer2);
}
