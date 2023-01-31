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

func string_reverse(s string) (string) {
	sslice:=make([]byte,len(s),len(s)+1)
	var x1,y1 byte
	for i := 0; i < int(len(s)/2) ; i++ {
		x1 = s[i]
		y1 = s[len(s) - i - 1]
		fmt.Printf("string_reverse():before XOR - x : %x - y : %x \n",x1,y1)
		x1 = x1 ^ y1
		y1 = x1 ^ y1
		x1 = x1 ^ y1
		fmt.Printf("string_reverse():after XOR - x : %x - y : %x \n",x1,y1)
		sslice[i] = x1
		sslice[len(s) - i - 1] = y1
	}
	for i,runecodepoint := range s {
		fmt.Printf("string_reverse(): string %d = %x\n",i,runecodepoint)
	}
	for i,runecodepoint := range sslice {
		fmt.Printf("string_reverse(): reversed string %d = %x\n",i,runecodepoint)
	}
	fmt.Printf("string_reverse() of %s = %s\n",s,string(sslice))
	return string(sslice)
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
	string_reverse("string")
}
