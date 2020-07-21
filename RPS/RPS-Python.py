import math
import random
pos=[-1,0,1]
def change(a=1):
    if a==-1:
        return 'Rock'
    elif a==0:
        return 'Paper'
    else:
        return 'Scissor'
    
def winning(com,pla):
    if (pla==1 and com==0) or (pla==0 and com==-1) or (pla==-1 and com==1):
        return True
    elif pla==com:
        return 'Uh Oh'
    else:
        return False

outcome=[-1,-1,-1,-1,0,0,0,1,1,1]

def highprob(a):
    rock=(a.count(-1)/len(a))
    paper=(a.count(0)/len(a))
    scissor=(a.count(1)/len(a))
    if rock>=paper and rock>=scissor:
        return 0
    elif paper>=rock and paper>=scissor:
        return 1
    else:
        return -1
    
state='lose'
u_wins=0
comp_wins=0

def main():
	while 1:
		n=int(input("insert as fllowing(Rock:-1 Paper:0 Scissor:1) : "))
		a=highprob(outcome)
		
		print('The computer chooses: ',change(a))
		if winning(a,n)==True:
			print("You win")
			u_wins+=1
		elif winning(a,n)==False:
			print("Computer wins")
			comp_wins+=1
		else:
			print("Tie")
	print('You:{} Computer:{}'.format(u_wins,comp_wins))
	outcome.append(n)
	outcome=outcome[1:]
	print()

if __name__ == "__main__":
	main()
    
