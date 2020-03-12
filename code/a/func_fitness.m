function [result] = func_fitness(pop,txt,star,tend)
%Ä¿±êº¯Êý
result = 0;
for i = 1:size(tend,1)
     result = result + abs( pop(1)*star(i) + pop(2)*txt(i) - tend(i));
end
end