library(ggplot2)
library(dplyr)
library(tidyr)
library(hrbrthemes)

#read csvs 
df1<- read.csv("C:\\Users\\kati.johnson\\Desktop\\formula1 data set\\lap_times.csv", header=TRUE)
df2<- read.csv("C:\\Users\\kati.johnson\\Desktop\\formula1 data set\\drivers.csv", header=TRUE)
df3<- read.csv("C:\\Users\\kati.johnson\\Desktop\\formula1 data set\\races.csv", header=TRUE)
#merging the csvs by driverID and raceID
f1 <- merge(df1,df2,by="driverId")
f2 <- merge(f1,df3,by="raceId")

#creating a dataframe with data only for Lewis Hamilton
hamdf<- f2[f2$'surname'=='Hamilton',]

#creating another dataframe with only the columns needed for the visual
hamdf2 <- subset(hamdf, select=c("milliseconds", "year"))
#dividing milliseconds by 1000 to create a seconds column (for better visualization)
hamdf2 <- hamdf2%>% 
  mutate(seconds = milliseconds / 1000)
#creating another dataframe with the average lap seconds per year
hamdf2 = hamdf2 %>% group_by(year) %>% summarise(mean_seconds = mean(seconds))
#plot size sets line thickness // lineend sets roundsness of the line // ggtitle sets title // labs sets axis labels and colour is legend label
ggplot() + geom_line(data = hamdf2, aes(x = year, y = mean_seconds, colour=mean_seconds), size=5, lineend = "round")+ ggtitle("Lewis Hamilton Average Lap Time by Racing Year")+labs(y = "Average Seconds", x = "Racing Year", colour = "Average Seconds")

