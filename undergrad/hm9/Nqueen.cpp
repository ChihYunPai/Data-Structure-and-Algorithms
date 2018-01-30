   // Queen_Game.cpp : Defines the entry point for the console application. 
    #include <iostream> 
    using namespace std; 
    class chess_block 
    { 
    public: 
        bool bQueen; 
        chess_block() 
        { 
            bQueen=false; 
        } 
    }; 
    bool IsSafeToPutQueen(int nRow, int nCol,chess_block **Chess_Board,int n ) 
    { 
        // We need to check for three directions upper left diagonal, lower left diagonal, and left horizontally; 
        int nTempColLeft=nCol-1; int nTempBelowRow=nRow+1;int nTempAboveRow=nRow-1; 
        bool bSafe=true; 
        // 
        while(nTempColLeft>=0 || nTempBelowRow<n || nTempAboveRow>=0) 
        { 
            if( ((nTempAboveRow>=0)&&(nTempColLeft>=0)&&(Chess_Board[nTempAboveRow][nTempColLeft].bQueen==true))    /*Left Upper Diagonal*/ 
                ||((nTempBelowRow<n)&&(nTempColLeft>=0)&&(Chess_Board[nTempBelowRow][nTempColLeft].bQueen==true))/*Left Lower Diagonal*/ 
                ||((nTempColLeft>=0)&&(Chess_Board[nRow][nTempColLeft].bQueen==true)))      /*Left Block*/ 
            { 
 
                bSafe=false; 
                break; 
 
            } 
            else 
            { 
 
                nTempColLeft--; 
                nTempAboveRow--; 
                nTempBelowRow++; 
            } 
        } 
        return bSafe; 
    } 
 
    chess_block **PrepareTheChessBoard(int n)//Allocate memory for n*n blocks 
    { 
        //chess_block **Chess_Board= (chess_block **)malloc(n*sizeof(chess_block *)); 
 
        chess_block **Chess_Board= new chess_block *[n]; 
 
        for(int i=0;i<n;i++) 
        { 
 
            Chess_Board[i]=new chess_block[n]; 
 
        } 
        for(int nColumn=0;nColumn<n;nColumn++) 
        { 
            for(int nRow=0;nRow<n; nRow++) 
            { 
 
                Chess_Board[nRow][nColumn].bQueen=false; 
            } 
        } 
        return Chess_Board; 
    } 
    void DestroyTheChessBoard(chess_block **Chess_Board,int n) 
    { 
        for(int i=0;i<n;i++) 
        { 
            delete [](Chess_Board[i]); 
 
        } 
        delete [](Chess_Board); 
    } 
 
    void PrintPositionsOfQueens(chess_block **Chess_Board,int n) 
    { 
 
        for(int nColumn=0;nColumn<n;nColumn++) 
        { 
            for(int nRow=0;nRow<n; nRow++) 
            { 
                if(Chess_Board[nRow][nColumn].bQueen==true)//Put The Queen Here 
                { 
 
                    cout<<"Column No.:   "<<nColumn   <<"               "<<"Row Number:   "<<nRow<<"\n"; 
                } 
 
            } 
        }     
 
    } 
    void ArrangeQueensOnBoard(chess_block **Chess_Board,int n) 
    { 
        bool bBackTrack=false; 
        int nRow=0; 
        for(int nColumn=0;nColumn<n;nColumn++) 
        { 
            for(nRow=0;nRow<n; nRow++) 
            { 
 
                if(IsSafeToPutQueen(nRow,nColumn,Chess_Board,n)) 
                { 
                    if(bBackTrack && Chess_Board[nRow][nColumn].bQueen==true) 
                    { 
                        Chess_Board[nRow][nColumn].bQueen=false; 
                        bBackTrack=false; 
                        continue; 
                    } 
                    else if(!bBackTrack) 
                    { 
                        Chess_Board[nRow][nColumn].bQueen=true; 
                        break;//Now Move to Next Col 
                    } 
                } 
            } 
            if(nRow ==n && Chess_Board[n-1][nColumn].bQueen==false)//means we need to backtrack 
            { 
                nColumn--; 
                if(nColumn<0) 
                { 
                    cout<<"THis combination can't place the queen "; 
                    break; 
                } 
                nColumn--; 
                bBackTrack=true; 
            } 
 
        } 
 
    } 
    int _tmain(int argc, int* argv[]) 
    { 
        while(1)//Don't be offended for this while loop it is only for keeping the command prompt window on the screen always 
        { 
            int n=0; 
            cout<<"Enter the value of N"<<"\n"; 
            cin>>n; 
            chess_block **Chess_Board=NULL; 
            Chess_Board=PrepareTheChessBoard(n); 
            if(Chess_Board == NULL) 
            { 
                return 0; 
 
            } 
            ArrangeQueensOnBoard(Chess_Board,n); 
            PrintPositionsOfQueens(Chess_Board,n); 
            DestroyTheChessBoard(Chess_Board,n); 
            Chess_Board=NULL; 
        }  
 system("pause");
        return 0; 
    } 
