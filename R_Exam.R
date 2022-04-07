#1. Write a R program to create a sequence of numbers from 20 to 50 and find the mean
#of numbers from 20 to 60 and sum of numbers from 51 to 91.
print("Sequence of number from 20 to 50:")
print(seq(20,50))
print("mean of number from 20 to 60:")
print(mean(20:60))
print("sum of number from 51 to 91:")
print(sum(51:91))


#2.  Write a R program to print the numbers from 1 to 100 and print "Fizz" for multiples
#of 3, print "Buzz" for multiples of 5, and print "FizzBuzz" for multiples of both.
for(n in 1:100){
  if (n %% 3 == 0 & n %% 5 == 0){print("FizzBuzz")}
  else if( n%% 3 ==0) {print("Fizz")}
  else if( n%% 5 == 0) {print("Buzz")}
  else print(n)
}
