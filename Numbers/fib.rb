def fib n
  if n==0
    0
  elsif n==1
    1
  else
    fib(n-1) + fib(n-2)
  end
end

puts fib(1),fib(2), fib(3), fib(4), fib(5), fib(6), fib(7)