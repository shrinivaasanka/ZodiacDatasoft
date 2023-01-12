#include <coroutine>
#include <iostream>
#include <cstdlib>

using namespace std;

struct task
{
	struct promise_type
	{
		task get_return_object() { return {}; }
		std::suspend_never initial_suspend() { return {}; }
		std::suspend_never final_suspend() noexcept { return {}; }
		void return_void() {}
		void unhandled_exception() {}
	};
	bool await_ready() { return false; }
	void await_suspend(std::coroutine_handle<> crh)
	{
		return;
	}
	void await_resume() {}
};

task coroutine1(int i);
task coroutine2(int i);

task coroutine1(int i)
{
	cout<<"coroutine1():"<<i<<endl;
	if (i == 1000)
		std::exit(0);
	co_await coroutine2(++i);
}

task coroutine2(int i)
{
	cout<<"coroutine2():"<<i<<endl;
	if (i == 1000)
		std::exit(0);
	co_await coroutine1(++i);
}

int main()
{
	int i=0;
	while(true)
	{
		task x1 = coroutine1(i);
		task x2 = coroutine2(i);
	}
}
