def data_comparison(data_list):
    if data_list:
        sort_data_list=sorted(data_list)
        if len(sort_data_list)%2 == 0:
            average_data_list=(sort_data_list[len(sort_data_list)/2]+sort_data_list[len(sort_data_list)/2-1])/2
        else:
            average_data_list=sort_data_list[len(sort_data_list)/2]

        if data_list[0] !=0:
	    print average_data_list, abs(average_data_list-data_list[0])/float(data_list[0])*100
            return abs(average_data_list-data_list[0])/float(data_list[0])*100
  
if __name__=='__main__':
    a=[1,2,3]
    print data_comparison(a)
    

