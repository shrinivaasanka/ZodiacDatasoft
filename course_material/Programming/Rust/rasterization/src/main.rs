fn main() {
    let number_to_factorize=1000; 
    rasterize_hyperbolic_arc(number_to_factorize);
}

fn rasterize_hyperbolic_arc(num_fact: i64)
{
    for y in 1..num_fact-1
    {
        let xtile_start = num_fact/y;
        let xtile_end = num_fact/(y+1);
        println!("tile segment {y}: from {xtile_start} to {xtile_end}");
        binary_search(num_fact,xtile_end,y,xtile_start,y);
    }
}

fn binary_search(num_fact:i64,xl:i64,yl:i64,xr:i64,yr:i64)
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
