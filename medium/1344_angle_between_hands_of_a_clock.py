def angleClock(hour: int, minutes: int) -> float:
  '''
    Gameplan
    ~~~~~~~~~
        - Turn the minutes and numbers into degrees 
            - There are 30 degs in an hour (h * 30)
            - There are 6 degs in a minute (m * 6)
            - The hour moves between the current hour and next hour
              in correlation to where the minute hand is.
                - 7:30 -> 7 is in the middle between 7 & 8 or 7.50
                - 5:15 -> 5 is a quarter of the way between 5 & 6 or 5.25
                - hour = hour + (minute/12)
        - Find the absolute difference between the two angles
            - | hourAngle - minuteAngle |
        - Take the acute angle
            - if the angle is bigger than half of the circle we take the bigger one
            return 360 - degreeFound
    '''
      
  # Turn hours and minutes into degrees
  hour = (hour + (minutes/60)) * 30
  minutes *= 6
      
  # Find the difference
  acuteAngle = abs(hour - minutes)
      
  # Check if the angle is more than half the circle, if so return the smaller
  if acuteAngle > 180:
      return 360 - acuteAngle
  return acuteAngle


print(angleClock(12, 30))
print(angleClock(3, 30))
print(angleClock(3, 15))
                                                                                                                                                                                                                                                                                                  
