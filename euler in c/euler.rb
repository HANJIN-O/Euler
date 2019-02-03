class Euler
	def euler1(first, last)
		@first = first
		@last = last
		@sum = 0
		x=(@fisrt.to_i..@last.to_i)
		x.each do |num|
		@sum += num if num%3==0 || num%5==0
		end
		puts @sum
	end

	def euler2
		@level = 1
		@sum = 2
		fibo = [1,2]
		while fibo[@level] <= 4000000
			@level += 1
			fibo << fibo[@level-1] + fibo[@level-2]
			@sum += fibo[@level] if fibo[@level]%2==0
		end
		puts @sum
	end

	def euler3
		x=600851475143
		aliquot=[]
		primefac=[]
		(2..x).each do |num|
			if x%num==0
				aliquot << num
			end
		end
		#for i in 0
		
	end

	def euler4
		num=[]
		pali=[]
		for a in 100..999
			for b in 100..999
				num << a*b
				num.to_s.split(//).each do |word|
					pali << word
					if pali[0]==pali[pali.size-1]&&pali[1]==pali[pali.size-2]&&pali[2]==pali[pali.size-3]
						puts pali+" is palindrome"
					else
						pali = []
					end
				end
				num = []
			end
		end
	end
end