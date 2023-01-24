package main

import "fmt"

func xor_swap(x1,y1 int) (int,int) {
	fmt.Println("---------xor_swap()------------")
	fmt.Printf("before XOR - x : %d - y : %d \n",x1,y1)
	x1 = x1 ^ y1
	y1 = x1 ^ y1
	x1 = x1 ^ y1
	fmt.Printf("after XOR - x : %d - y : %d \n",x1,y1)
	return x1,y1
}

func xor_swap_goroutine(x1,y1 int,channelx,channely chan int) {
	fmt.Println("---------xor_swap_goroutine()------------")
	fmt.Printf("before XOR - x : %d - y : %d \n",x1,y1)
	x1 = x1 ^ y1
	y1 = x1 ^ y1
	x1 = x1 ^ y1
	fmt.Printf("after XOR - x : %d - y : %d \n",x1,y1)
	channelx <- x1
	channely <- y1 
}

func main() {
	var x,y int =1,2
	fmt.Printf("x : %d - y : %d \n",x,y)
	x,y=xor_swap(x,y)
	fmt.Printf("after xor_swap() === x : %d - y : %d \n",x,y)
	var channelx=make(chan int)
	var channely=make(chan int)
	go xor_swap_goroutine(x,y,channelx,channely)
	x= <-channelx	
	y= <-channely	
	fmt.Printf("after xor_swap_goroutine() === x : %d - y : %d \n",x,y)
}
