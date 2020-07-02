  

def main():
    e_pace = 8*60+15 ## easy pace in seconds
    t_mile = 7*60+12 ## tempo in seconds
    # I run 1 mile at Easy Pace + 3 Miles at tempo + 1 more at Easy Pace
    total_min = (e_pace+3*t_mile+e_pace)/60 #Total in minutes
    ini_hour_m = 6*60+52 ## departure time in minutes
    return_hour_h = (total_min+ini_hour_m)/60
    #print(return_hour_h)
    h = int(str(return_hour_h).split('.')[0])
    m = int(float('0.'+str(return_hour_h).split('.')[1][0:2])*60)
    
    print('Eu voltarei para casa as {}:{}'.format(h,m))

if __name__ == "__main__":
    main()
