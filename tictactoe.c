#include <stdio.h>
#include <stdlib.h>

//Function prototypes
void mainmenu(void);
void createboard(int[]);
int checkindex(int,int[],int);
int checkwin(int position[]);

int main(){
	
	char runagain;
	
	mainmenu();
	
	do{
		int count=0,symbol,player,index=0,winner=0;
		int i,position[9];
		
		for (i=0;i<9;i++){
			position[i]=' ';		
		}
				
		while(count<=8 && winner!=1){
			
			createboard(position);
			
			//Player turn
			if (count%2==0){
				symbol='X';
				player=1;
			}
			else{
				symbol='O';
				player=2;
			}
			
			count++;//counts the number of moves made, cannot exceed 8
			
			index=checkindex(index,position,player);
			
			position[index]=symbol; //Placing symbol marker at player-specified location
					
			if(count>=5){
				winner=checkwin(position); //checks if game has been won
			}
		
		}
		createboard(position);
		position[index]=symbol;
		
		if (winner==1){
			printf("\nPlayer %d has won the game. Congratulations!",player);
		}
		else{
			printf("\nDraw! Good game!");
		}
		
		do{
			printf("\nWould you like to play again?(y/n): ");
			scanf(" %c",&runagain);
		}while(runagain!='y' && runagain!='Y' && runagain!='n' && runagain!='N');
		
	}while(runagain=='y' || runagain=='Y'); //allows players to play the game again
}

//Function Definitions

//Main menu
void mainmenu(void){
	
	char playgame;
	
	do{
		printf("Welcome to Tic Tac Toe Game! This is a fun and easy game! Would you like to play?(y/n): ");	
		scanf(" %c",&playgame);	
	}while(playgame!='y' && playgame!='n' && playgame!='Y' && playgame != 'N');
	
	if (playgame=='y' || playgame == 'Y'){
		printf("This is our board!\n");
		printf("\n");
		printf("0|1|2\n");
		printf("------\n");
		printf("3|4|5\n");
		printf("------\n");
		printf("6|7|8\n");
		printf("\nThe different index positions correspond to where you place your marker(X/O)\n");
	}
	else{
		exit(0);
	}
}

//Create board
void createboard(int position[]){
	printf("\n");
	printf("%c|%c|%c\n",position[0],position[1],position[2]);
	printf("------\n");
	printf("%c|%c|%c\n",position[3],position[4],position[5]);
	printf("------\n");
	printf("%c|%c|%c\n",position[6],position[7],position[8]);
}

//Error checking index positions
int checkindex(int index,int position[],int player){
	do{
		printf("\nIts your turn player %d\nWhich index will be your next move?: ",player);
		scanf("%d",&index);
	}while(index<0||index>8||position[index]=='X'||position[index]=='O');
	
	return(index);
}

//Checks if you have won the game; 1 and 0 act like true/false conditions
int checkwin(int position[]){
	if (position[0] == position[1] && position[0] == position[2] && position[0]!=' ') //first row
        return 1;

    else if (position[3] == position[4] && position[3] == position[5] && position[3]!=' ') //second row
        return 1;

    else if (position[6] == position[7] && position[6] == position[8] && position[6]!=' ') //third row
        return 1;

    else if (position[0] == position[4] && position[0] == position[8] && position[0]!=' ') //left-right diagonal
        return 1;

    else if (position[2] == position[4] && position[2] == position[6] && position[2]!=' ') //right-left diagonal
        return 1;

    else if (position[2] == position[5] && position[2] == position[8] && position[2]!=' ') //right column
        return 1;

    else if (position[1] == position[4] && position[1] == position[7] && position[1]!=' ') //middle column
        return 1;

    else if (position[0] == position[3] && position[0] == position[6] && position[0]!=' ') //left column
        return 1;

    else
        return 0; //this is the condition where winner=0 and thus either the game will continue or result in a draw
	
}

