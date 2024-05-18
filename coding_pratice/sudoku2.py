def check_for_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            # print('yes')
            if grid[i][j] == 0 :
                return (i,j)
            
def check_if_exist(grid,col,row,num):
    #
	
	grid[col][row] = num
	print('number :' ,num)
	
	 	#checking if number present in same colmmn  
	for i in range(len(grid)):
		print("Comparing assinged value and checking if exists  in same column:",grid[col][row],grid[col][i])
		if grid[col][row] == grid[col][i+1] :
			return False
		# break
		#checking if number present in same row 
	for i in range(len(grid)):
		print("checking if value present in same row")
		if grid[col][row] == grid[i+1][row] :
			return False
                

		# check if number present in same 3x3 matrix 
	startRow = row - row % 3
	startCol = col - col % 3
	num = grid[col][row] 
	for i in range(3):
		for j in range(3):
			if grid[i + startRow][j + startCol] == num:
				return False
	return True
		
                                  
              
				
            


def solve_sudoku(grid):
	pos =  check_for_empty(grid)
	col, row  = pos
	print(col,row)
    
	# check if the value present at postiion exist  in row or col
	for i in range(len(grid)):
		num = i+1
		# print(num)
		# print(col,row)
		if check_if_exist(grid,col,row,num) :
			grid[col][row] = num
			print(num)

		
		
	    
       
    







grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
		[5, 2, 0, 0, 0, 0, 0, 0, 0],
		[0, 8, 7, 0, 0, 0, 0, 3, 1],
		[0, 0, 3, 0, 1, 0, 0, 8, 0],
		[9, 0, 0, 8, 6, 3, 0, 0, 5],
		[0, 5, 0, 0, 9, 0, 6, 0, 0],
		[1, 3, 0, 0, 0, 0, 2, 5, 0],
		[0, 0, 0, 0, 0, 0, 0, 7, 4],
		[0, 0, 5, 2, 0, 6, 3, 0, 0]]



solve_sudoku(grid)