
#define ldrpin A0
//File myf;
long adcCounts;
//char ar[100];
//int o=0;
//String bitr;
//int f=0,i=0,j=0;

void setup() {
  Serial.begin(9600);
  pinMode(ldrpin,INPUT);

}
void loop() {
  // put your main code here, to run repeatedly:
  
  adcCounts=analogRead(ldrpin);
  Serial.print(oi(adcCounts));
 
  delay(50);

}
char oi(long xval)
{
  if(xval>900){
    return '1';
  }
  else if(xval<=900){
    return '0';
  }
}
