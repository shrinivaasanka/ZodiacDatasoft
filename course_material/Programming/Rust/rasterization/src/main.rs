use std::env;
fn main() {
    let args: Vec<String>=env::args().collect();
    let number_to_factorize: i32=args[1].parse().unwrap(); 
    let rasterization: String=args[2].clone();
    rasterize_hyperbolic_arc(number_to_factorize,rasterization);
}

use rayon::prelude::*;
use foreach::*;
fn rasterize_hyperbolic_arc(num_fact: i32,rasterization: String)
{
    let mut y1 = 1..num_fact-1;
    let mut y2 = 1..num_fact-1;
    if rasterization=="sequential"
    {
        println!("rasterize_hyperbolic arc(): rasterization by sequential iterator");
        y1.foreach(|item,iter| {
            let mut xtile_start = num_fact/item;
            let mut xtile_end = num_fact/(item+1);
            println!("tile segment {item}: from {xtile_start} to {xtile_end}");
            binary_search(num_fact,xtile_end,item,xtile_start,item);
        });
    }
    if rasterization=="parallel"
    {
        println!("rasterize_hyperbolic arc(): rasterization by Rayon parallel iterator");
        y2.into_par_iter().for_each(|paritem| {
            let mut xtile_start = num_fact/paritem;
            let mut xtile_end = num_fact/(paritem+1);
            println!("tile segment {paritem}: from {xtile_start} to {xtile_end}");
            binary_search(num_fact,xtile_end,paritem,xtile_start,paritem);
        });
    }
}

fn binary_search(num_fact:i32,xl:i32,yl:i32,xr:i32,yr:i32)
{
    println!("binary seach of rasterized hyperbolic arc bow tilesegment xy = {num_fact}: {xl},{yl},{xr},{yr}");
    let mut xl_clone = xl.clone();
    let mut yl_clone = yl.clone();
    let mut xr_clone = xr.clone();
    let mut yr_clone = yr.clone();
    while xl_clone <= xr_clone  
    {
        let mut midpoint = (xl_clone + xr_clone) / 2;
        println!("Midpoint = {midpoint}");
        let mut factorcandidate = midpoint*yl_clone;
        println!("Factor candidate point : {factorcandidate}");
        if xl_clone==xr_clone
        {
             std::process::exit(1);
        }
        if factorcandidate==num_fact
        {
             println!("Factor point located : {midpoint} {yl_clone}");
        }
        if xl_clone*yl_clone==num_fact
        {
             println!("Factor point located : {xl_clone} {yl_clone}");
        }
        if xr_clone*yr_clone==num_fact
        {
             println!("Factor point located : {xr_clone} {yr_clone}");
        }
        if factorcandidate > num_fact
        {
             println!("factorcandiate > num_fact");
             xr_clone = xl_clone + midpoint;
        }
        else
        {
             println!("factorcandiate < num_fact");
             xl_clone = xl_clone + midpoint;
        }
    }
}
