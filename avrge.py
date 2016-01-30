def average(values):
    """
Printing average array.
example:
        average(values), where values = [1,3,4,5]
    """
    
    return sum(values)/len(values)

def matching(values):
    """
matching values[0] and average(values), output percentage
example:
        matching(values) #where values=[1,3,4,5]
        >> 250        
    """
    return abs(average(values)-values[0])/float(values[0])*100
  
def seach(values):
    if values != None and type(values[0]) == list:
        return matching(values)


if __name__=='__main__':
    a=[1,2,3]
    print seach(a)
    

