OPENQASM 2.0;  
						
include "qelib1.inc";   

qreg qubit[3]; 			
creg classicalbit[3];	


 z qubit[2];   		
 x qubit[2];			
 y qubit[2];			
 h qubit[2];          

 s qubit[0]; 			
 sdg qubit[0]; 		   
 t qubit[0]; 			
 tdg qubit[0]; 		

 					

ry(-pi/7) 	qubit[0];   


barrier qubit[0];
measure qubit[0] -> classicalbit[0];
