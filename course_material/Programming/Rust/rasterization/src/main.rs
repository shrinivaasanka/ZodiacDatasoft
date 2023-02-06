use std::env;
use std::io::*;
use std::time::*;
use rayon::prelude::*;
use foreach::*;

fn main() {
    let args: Vec<String>=env::args().collect();
    let number_to_factorize: i32=args[1].parse().unwrap(); 
    let range: i32=args[2].parse().unwrap();
    let rasterization: String=args[3].clone();
    factorize_multipleintegers(number_to_factorize,range,rasterization);
    stdout().flush().unwrap();
}

fn factorize_multipleintegers(num_fact:i32,range:i32,rasterization:String) {
    let mut i = 0;
    for i in 1..range {
        let mut systemtimebegin = SystemTime::now();
        let mut number_to_factorize = num_fact+i;
        let mut raster = rasterization.clone();
        println!("Factorization of {number_to_factorize} began in (nanoseconds): {:#?} ",systemtimebegin);
        rasterize_hyperbolic_arc(number_to_factorize,raster);
        let systemtimeend = SystemTime::now();
        let duration = systemtimeend.duration_since(systemtimebegin).unwrap(); 
        println!("Factorization of {number_to_factorize} was completed in (nanoseconds): {:#?} ",duration);
    }
}

#[inline]
fn rasterize_hyperbolic_arc(num_fact: i32,rasterization: String) -> i32
{
    let mut y1 = 1..num_fact-1;
    let mut y2 = 1..num_fact-1;
    if rasterization=="sequential"
    {
        let systemtimebegin = SystemTime::now();
        y1.foreach(|item,iter| {
            let mut xtile_start = num_fact/item;
            let mut xtile_end = num_fact/(item+1);
            //println!("tile segment {item}: from {xtile_start} to {xtile_end}");
            binary_search(num_fact,xtile_end,item,xtile_start,item);
        });
        let systemtimeend = SystemTime::now();
        let duration = systemtimeend.duration_since(systemtimebegin).unwrap(); 
        println!("Sequential Rasterization phase of factoring {num_fact} was completed in (nanoseconds): {:#?} ",duration);
        stdout().flush().unwrap();
    }
    if rasterization=="parallel"
    {
        let systemtimebegin = SystemTime::now();
        y2.into_par_iter().for_each(|paritem| {
            let mut xtile_start = num_fact/paritem;
            let mut xtile_end = num_fact/(paritem+1);
            //println!("tile segment {paritem}: from {xtile_start} to {xtile_end}");
            binary_search(num_fact,xtile_end,paritem,xtile_start,paritem);
        });
        let systemtimeend = SystemTime::now();
        let duration = systemtimeend.duration_since(systemtimebegin).unwrap(); 
        println!("Parallel Rasterization phase of factoring {num_fact} was completed in (nanoseconds): {:#?} ",duration);
        stdout().flush().unwrap();
    }
    return 1;
}

#[inline]
fn binary_search(num_fact:i32,xl:i32,yl:i32,xr:i32,yr:i32) -> Vec<i32> 
{
    //println!("binary seach of rasterized hyperbolic arc bow tilesegment xy = {num_fact}: {xl},{yl},{xr},{yr}");
    let mut xl_clone = xl.clone();
    let mut yl_clone = yl.clone();
    let mut xr_clone = xr.clone();
    let mut yr_clone = yr.clone();
    let mut factors = Vec::new();
    while xl_clone <= xr_clone  
    {
        let mut midpoint = (xl_clone + xr_clone) / 2;
        //println!("Midpoint = {midpoint}");
        let mut factorcandidate = midpoint*yl_clone;
        //println!("Factor candidate point : {factorcandidate}");
        //println!("===============================================================");
        if xl_clone==xr_clone
        {
             //std::process::exit(1);
             return factors;
        }
        if factorcandidate==num_fact
        {
             println!("Factor point located : {midpoint} {yl_clone}");
             factors.push(factorcandidate);
        }
        if xl_clone*yl_clone==num_fact
        {
             println!("Factor point located : {xl_clone} {yl_clone}");
             factors.push(xl_clone);
             factors.push(yl_clone);
        }
        if xr_clone*yr_clone==num_fact
        {
             println!("Factor point located : {xr_clone} {yr_clone}");
             factors.push(xr_clone);
             factors.push(yr_clone);
        }
        if factorcandidate > num_fact
        {
             //println!("factorcandiate > num_fact");
             xr_clone = xl_clone + midpoint;
        }
        else
        {
             //println!("factorcandiate < num_fact");
             xl_clone = xl_clone + midpoint;
        }
        //println!("===============================================================");
    }
    stdout().flush().unwrap();
    return factors;
}
