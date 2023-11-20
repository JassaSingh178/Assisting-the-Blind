I have created a new project for blind people to use pc. I have tried to make it voice controlled and automated. You can download the packages used in my project and run in vs code but you need to tune your microphone according to your system after clonning this repository, you just need to open the Mark.py file and tune these three commands listed below:
        r.pause_threshold = 0.5
        r.dynamic_energy_ratio = 1
        r.energy_threshold = 650
        System microphone sound = 55
        Pause threshold is the max seconds between gap of words after which it stops taking the command and executes the voice command
        dynamic energy ratio is the amplification of the voice command but note incressing it can also lead to amplification of the disturbances
        energy threshold is the minimum units of loudness that is required by microhone to detect the voice command and decreasing it can also detect surrounding less loud noises. You also need to tune the microphone input level for best voice command input performance. You need to also modify the code according to the songs added in the system and add its path and add their respective name in the code file i.e. Mark.py .
        
        
        
        You can contact me at linkedin if you need any assistance.
        My Linkedin : www.linkedin.com/in/jassa-singh15
