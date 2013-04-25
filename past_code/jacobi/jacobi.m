function x = jacobi(A, b, tol)
[n,m] = size(A);

x=zeros(n,1);

for i = 1:n
	C(i,:) = -A(i,:) / A(i,i);
	d(i) = -b(i)/A(i,i);
end

#C = -A .* ( 1/diag(A) * ones(1,n) ) + eye(n,n)
#d =  b .*   1/diag(A);

C = C + eye(n);

norma_C = norm(C,Inf);

error = Inf;
while error > tol
	y = x;
	x = C*x + d(:);
	error = (norma_C / (1 - norma_C))  * norm(x-y, Inf);	
end

