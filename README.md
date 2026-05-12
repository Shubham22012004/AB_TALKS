Day 11
today I solved the DSA Question -> move zeros

in this we have to move the zero either at the end or at the beginning

1st method - By taking an extra list
  in this you will take an list of the same size of provided list
  you will add the all non-zero elements in list intitally then add zero 

2nd method -  optimal way i.e you make the changes in the given list
  this can be done by taking two pointer - slow and fast
  
  conditions
    if fast points 0 -> move the faster pointer
    if slow points non-zero element -> move the slow poiter
    else : swap the pointer elements

in both the situtaion you will maintain the order of elements