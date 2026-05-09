class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        #Step1 - Find the no of layers
        layers = min(m,n)//2
        for layer in range(layers):
            arr = []
            #TOP - fetching and storing TOP row elements
            i = layer
            for j in range(layer,n-1-layer+1):
                arr.append(grid[i][j])

            #RIGHT - fetching and storing RIGHT columns elements
            j = n-1-layer
            for i in range(layer+1,m-1-layer-1+1):
                arr.append(grid[i][j])

            #BOTTOM - fetching and storing BOTTOM row elements
            i = m-1-layer
            for j in range(n-1-layer,layer-1,-1):
                arr.append(grid[i][j])
            
            #LEFT - fetching and storing LEFT columns elements
            j = layer
            for i in range(m-1-layer-1,layer+1-1,-1):
                arr.append(grid[i][j])
            
            #rotate arr k-times
            l = len(arr)
            # our k will be k%l in order to normalize the roations
            arr[:] = arr[k%l:]+arr[:k%l]

            idx=0 #iterator for list arr
            #TOP - putting back new values of TOP row elements
            i = layer
            for j in range(layer,n-1-layer+1):
                grid[i][j]=arr[idx]
                idx+=1

            #RIGHT - putting back new values of RIGHT columns elements
            j = n-1-layer
            for i in range(layer+1,m-1-layer-1+1):
                grid[i][j]=arr[idx]
                idx+=1

            #BOTTOM - putting back new values of BOTTOM row elements
            i = m-1-layer
            for j in range(n-1-layer,layer-1,-1):
                grid[i][j]=arr[idx]
                idx+=1
            
            #LEFT - putting back new values of LEFT columns elements
            j = layer
            for i in range(m-1-layer-1,layer+1-1,-1):
                grid[i][j]=arr[idx]
                idx+=1
        
        return grid