
# RZ/V2L EVKit Quick Setup Overview

Setting up the RZ/V2L platform involves two main tasks:

1. **Installing the RZ/V2L AI SDK on an Ubuntu host machine** — used for model conversion and deployment via the GUI.
2. **Preparing the RZ/V2L EVKit** — including hardware connections and SD card setup.

---

## 🔧 Setup Overview

For detailed instructions, refer to the [RZ/V AI GitHub repository](https://renesas-rz.github.io/rzv_ai_sdk/latest/getting_started.html). Be sure to select the latest version from the top-left dropdown. Here's a quick summary:

### ✅ Step-by-Step Summary

- **Steps 1–2**: Acquire the board and required components (see table below).
- **Steps 3–5**: Download the RZ/V2L AI SDK and set up the Docker container. For optimal performance, use **DRP-AI TVM v2.5**.
- **Step 7**: Format the microSD card and flash the bootloader and Yocto image. This is essential for new boards or SDK updates. Ensure you have partitioned your microsD card appropriately.
- **Final Setup**: Connect the board as shown in *Figure below*. Note: SW1 & SW11 switch orientation depends on your bootloader choice (eSD/eMMC).
- **Shutdown**: Follow the [safe shutdown procedures](https://renesas-rz.github.io/rzv_ai_sdk/latest/appendix.html#A3).


> **Note:** On your board, check if libtvm_runtime.so exists under /usr/lib64 directory of the root filesystem of the board. If not copy from docker ‘/drp-ai_tvm/obj/build_runtime/V2L/’ folder path to board under /usr/lib64 via secure copy.

---

## 🧰 Required Equipment

| **Component**           | **Details**                                                                 |
|------------------------|------------------------------------------------------------------------------|
| **RZ/V2L EVKit**        | Main board for AI demo execution                                            |
| **USB Type-C Cable**    | Connects power adapter to the board                                         |
| **AC Adapter**          | Powers the board                                                            |
| **USB Camera**          | For visualizing inference results                                           |
| **microSD Card**        | Minimum 4GB free space<br>*Recommended:* Transcend USH-I microSD 300S 16GB  |
| **Linux PC (Host)**     | For SDK installation and SD card setup<br>*OS:* Ubuntu 20.04                |
| **SD Card Reader**      | Used to flash bootloader and OS image                                       |
| **USB Hub**             | For connecting keyboard and mouse                                           |
| **USB Keyboard & Mouse**| For terminal and GUI interaction                                            |
| **HDMI Monitor**        | *Optional:* Needed for standalone GUI apps                                  |
| **Micro HDMI Cable**    | Connects board to HDMI monitor                                              |
| **Ethernet Cable**      | Enables board-host communication                                            |

---

## 🔌 Hardware Connectivity

To run the demo end-to-end with GUI visualization, ensure the following connections:

- `RZ/V2L → Ethernet → Host PC`
- `RZ/V2L → USB Camera`
- `RZ/V2L → USB-C → Power Adapter`

### Hardware Setup Diagram

![Renesas TAO Integration Overview](../../docs/assets/RZ_V2L_HW_setup.png)

---

## 📌 Notes

- This page serves as a **quick-start checklist** to ensure you have the right equipment and understanding before setup.
- For scripts, troubleshooting, and advanced usage, always refer to the [RZ/V AI GitHub repository](https://renesas-rz.github.io/rzv_ai_sdk/latest/).

---

