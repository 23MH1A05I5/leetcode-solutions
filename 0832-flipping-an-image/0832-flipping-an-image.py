class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for img in image:
            left=0
            right=len(img)-1
            while left<right:
                if left>=right:
                    break
                img[left],img[right]=img[right],img[left]
                left+=1
                right-=1
            for i in range(len(img)):
                if img[i]==0:
                    img[i]=1
                else:
                    img[i]=0
        return image


        