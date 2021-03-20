# capbot-siic
Repository to hold code for the [cap-bot](https://github.com/aryankargwal/cap-bot) varient that is being presented at the SIIC Defence Hackathon 2021.
<br>

## Problem Inspiration<br>
<img src="assets/cctv_system.jpg" width = "500px"><br>
A plethora of surveillance devices are being used by the Defense Services for supervision and monitoring. However, most of them are manually operated at the cost of enormous amounts of time and manual labour.
<br>

## Problem Description<br>
Present state-of-the-art Surveillance Devices require both consistent manual assistance and time for their successful operation. This results in a considerable loss of manual and technical resources.
<br>

## Proposed Solution<br>
We propose a Deep Learning Application that will be able to solve the above mentioned problems. 
- Our application named ‘Cap-Bot’ is capable of running Image Captioning on multiple CCTV footages and storing the captions along with the camera number and the time of capture in a convenient log.<Br>
<img src = "assets/cameraui.jpg" width = "500px"><br>
- The file of saved captions can then be used to look up for incidents from any instant of time just by entering a few keywords.  The returned camera number and time slot can then be used to obtain the required CCTV footage.<br>
<img src = "assets/search_tab.png" width = "500px"><br>

## Advantages and Features
- Interface to map CCTV Location in a defined area and eventually help single out points of interest.<br>
<img src = "assets/locations.png" width = "500px"><br>
- Since our model relies on Deep Learning, the time can be reduced considerably as we are resorting to an automatic searching operation.<br>
<img src = "assets/dl.png" width = "500px"><br>
- Since the information is purely textual, the encryption of information is way easier than pictorial.<br>
<img src = "assets/encrypt.png" width = "500px"><br>
  
## Steps of Deployment
- [x] Training the Model
- [x] Write the Search Module
- [x] Captioning UI
- [x] Search UI
- [x] Perfecting Search feature 
- [x] Resolving Backend
- [x] Encryption of Generation Captions<br>
<i>Extra Feature</i>
- [ ] CCTV Localization with results


## Using the deployed version of the web application
Please download the <a href = "https://drive.google.com/drive/folders/10RaV7DTsFVgdYeJZIyveyeJKhfvFiKT2?usp=sharing">Model Checkpoints</a> and move the file to the <a href = "https://github.com/aryankargwal/capbot2.0/tree/main/camera">camera</a> folder.

- Cloning the Repository: 

        git clone https://github.com/aryankargwal/capbot2.0
- Entering the directory for captioning: 

        cd capbot2.0/camera
- Running the captioning web application:

        streamlit run feed.py
- Entering the directory for searching: 

        cd capbot2.0/camera
- Running the searching web application:

        streamlit run search.py
        
<hr>

## License
This project is under the Apache License. See [LICENSE](LICENSE) for Details.

## Contributors

<table>
<tr align="center">
<td>

Aryan Kargwal

<p align="center">
<img src = "https://media-exp1.licdn.com/dms/image/C4E03AQF-jQx69fbYiw/profile-displayphoto-shrink_200_200/0/1610317317984?e=1621468800&v=beta&t=DA1te6zagqlPJarwqm3iDawBUn3n2QCXesSi75httIU"  height="120" alt="Aryan Kargwal">
</p>
<p align="center">
<a href = "https://github.com/aryankargwal"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/aryan-kargwal-2550561a2/">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>

<td>

Indira Dutta

<p align="center">
<img src = "https://media-exp1.licdn.com/dms/image/C5103AQE5CkDeJQ8mmQ/profile-displayphoto-shrink_200_200/0/1573304359382?e=1621468800&v=beta&t=-uptIYAUuX4JoRcYazPr6R_HiKrZxeMjndRtMuc3YEQ"  height="120" alt="Indira Dutta">
</p>
<p align="center">
<a href = "https://github.com/indiradutta"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/indira-dutta-775445197/">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>

<td>

Kunal Mundada

<p align="center">
<img src = "https://media-exp1.licdn.com/dms/image/C5603AQE_ev0fCPT0Uw/profile-displayphoto-shrink_200_200/0/1581639518725?e=1621468800&v=beta&t=ievx9n9yClEOkaW6nQw5CT8AhE6bWVgWh-We5nK9_vY"  height="120" alt="Rusali Saha">
</p>
<p align="center">
<a href = "https://github.com/AlKun25"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/kunalmundada/">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>

<td>

Srijarko Roy

<p align="center">
<img src = "https://media-exp1.licdn.com/dms/image/C5603AQFCctkhnahzoA/profile-displayphoto-shrink_200_200/0/1592055341403?e=1621468800&v=beta&t=NkSQlaxskFl2fO-34vIp4D45vI7mOWwyWyjiiuIu73A"  height="120" alt="person">
</p>
<p align="center">
<a href = "https://github.com/srijarkoroy"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/srijarko-roy-9193751b0/">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>
  </table>
</tr>
  </table>


<p align="center">
crafted with <span style="color: #8b0000;">&hearts;</span> by team <b>Missing-Colon</b>
</p>
