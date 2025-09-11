### Quick Deploy (MCU) 

These are **prebuilt application example(s)** for Renesas EK-RA8D1. 


Two methods will be provided for each application.
1. A `.Hex` file provided in the directory can be flashed onto the board via Renesas Flash Programmer ([RFP](https://www.renesas.com/en/software-tool/renesas-flash-programmer-programming-gui?srsltid=AfmBOor9zRK_Bnz-5BXw7-o--o9hc7EWvndavQA7Rb7EMrKl2CX_rNH3#overview)).
2. Project source code that can be imported into E2 studio, built and flashed onto the board.

### Hardware Setup

Please ensure to have completed board bring up as described [here](/board_bringup/ra8d1/readme.md).

### Quick Deploy Steps


### 1. .Hex Flash via RFP

For quick testing `.Hex` file is provided, Renesas Flash programmar GUI can be quickly leveraged to flash the board without requiring a build/compilation on E2 studio.
RFP can be downloaded from [here](https://www.renesas.com/en/software-tool/renesas-flash-programmer-programming-gui?srsltid=AfmBOorL2b7Pw4k8xf33x_w_01KkrRqLfTJdHVX9PFqi4JLV81HyxYCI)






### 2. Project build via E2 studio

In order to build and flash the project, please ensure that you have appropriate FSP version and supported libraries installed. 

**Software prerequisites** <br>

**FSP version:** 5.2.0 only, installable [here](https://github.com/renesas/fsp/releases/tag/v5.2.0) <br>
**E2 studio:** 2024.01.01 or later


1. Open e2 studio and select a workspace
2. Click File -> Import -> Existing Projects to Workspace
3. Select archive file -> Browse .zip file -> Click Finish
4. Select Project from project explorer tab --> Click Build project (🔨 Icon) --> Build complete with no errors
5. Select project --> Click Debug --> Debug as --> Renesas GDB Hardware Debugging
6. Application should be flashed on board --> Click next icon twice to vizualize results
