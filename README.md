# Li-Fi
a project on transmission of data from one device to another device with light medium.

Basic working of Li-Fi : The light emitter or light
 source is on one end and a photo detector on the
 other. Both sender and receiver has both the
 modules in order to execute data forwarding and
 data receiving. The sender converts the data into
 binary format and sends it to the receiver by the
 light emitter and the binary code is then received to
 build up a message.

Transmission : The transmission module receives
 data from the user through the use of an user
 interface which is then sent to the encoder, a flag is
 then added to identify the blocks of data(the flag
 used in this specific project is 44 i.e.,”1000 1000” as
 per the KEY mentioned earlier). which is then sent
 to the receiver through the light source by
 adjusting the current flow of the LED to turn it on
 and off for differentiating 1s and 0s.
 
 Encoder :  it encodes the data that is to be sent to
 the receiver into binary data using a specific KEY to
 encrypt the data considering the privacy of the
 sender and to prevent the data from data loss. ECC
 is later appended at the end and beginning of the
 data being transferred to identify and recover data
 in case of data loss

 Receiver : Module with the help of LDR where the
 binary value ‘0’ is considered when the circuit
 around the LDR is broken i.e., the time duration
 when the light is not appearing over the LDR, the
 binary value ‘1’ is considered when the circuit
 around the LDR is complete i.e., the time duration
 when the light falls over the sensor.
 
 Decoder : The decoder is a sub-module of receiver
 module where it receivers the raw binary data from
 the receiver module and converts it into its
 respective format with the help of KEY from the
 receiver side as mentioned before to decrypt the
 encrypted data
<br />
receiver side circuit:<br />
<img src="https://github.com/Hariharan200930/Li-Fi/assets/129237134/e30624af-9a2c-4e39-8fa7-fa468af83d91" width="400" height="400" />
<br />
sender side circuit: <br />
<img src="https://github.com/Hariharan200930/Li-Fi/assets/129237134/3ec8840e-be53-4bc3-a2cf-971ed56ec4b5" width="400" height="400" />
<br />
receiver side output:<br />
<img src="https://github.com/Hariharan200930/Li-Fi/assets/129237134/429644ef-8c65-47e5-ac80-69beef83a8da" width="500" height="500" /><br />
intermediate code:<br />
<img src="https://github.com/Hariharan200930/Li-Fi/assets/129237134/d57bf61b-3ef7-4304-90ab-c619f4f22b54" width="500" height="500" /><br />

