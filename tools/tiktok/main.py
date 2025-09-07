import time
import pyautogui
import cv2
import numpy as np
from datetime import datetime

class PreparationManager:
    def __init__(self):
        pass
        
    def log_message(self, message):
        """Affiche un message avec timestamp"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {message}")
    
    def wait_with_countdown(self, seconds, message="Waiting"):
        """Wait with visible countdown"""
        self.log_message(f"{message} - {seconds} seconds...")
        for i in range(seconds, 0, -1):
            print(f"\r⏳ {i} seconds remaining...", end="", flush=True)
            time.sleep(1)
        print()
    
    def click_on_image(self, image_path, confidence_threshold=0.7, max_attempts=30, wait_time=1):
        """Function to find and click on an image"""
        attempt = 1
        
        while attempt <= max_attempts:
            self.log_message(f"Attempt {attempt} searching for: {image_path}")
            
            # Take screenshot
            screen = np.array(pyautogui.screenshot())
            screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
            
            # Load target image
            target = cv2.imread(image_path)
            
            if target is None:
                self.log_message(f"❌ Could not load image {image_path}")
                return False
            
            # Search for the image
            result = cv2.matchTemplate(screen, target, cv2.TM_CCOEFF_NORMED)
            _, score, _, position = cv2.minMaxLoc(result)
            
            if score > confidence_threshold:
                # Calculate center of image
                h, w = target.shape[:2]
                center_x = position[0] + w//2
                center_y = position[1] + h//2
                
                time.sleep(0.5)
                pyautogui.click(center_x, center_y)
                self.log_message(f"✅ Image found and clicked: {image_path} (score: {score:.2f})")
                return True
            else:
                self.log_message(f"⚠️ Image not found (best score: {score:.2f})")
                if attempt < max_attempts:
                    time.sleep(wait_time)
                attempt += 1
        
        self.log_message(f"❌ Failed to find {image_path} after {max_attempts} attempts")
        return False
    
    def run_preparation_sequence(self):
        """Execute ONLY the preparation actions"""
        self.log_message("🎬 Starting TikTok Studio preparation sequence...")
        
        # 1. Click on apps.png
        self.log_message("Step 1: Searching and clicking on apps.png")
        if not self.click_on_image("assets/images/apps.png"):
            self.log_message("❌ Failed to click on apps.png")
            return False
        
        # 2. Click on close_all.png
        self.log_message("Step 2: Searching and clicking on close_all.png")
        if not self.click_on_image("assets/images/close_all.png"):
            self.log_message("❌ Failed to click on close_all.png")
            return False
        
        # 3. Click on tiktok_studio.png
        self.log_message("Step 3: Searching and clicking on tiktok_studio.png")
        if not self.click_on_image("assets/images/tiktok_studio.png"):
            self.log_message("❌ Failed to click on tiktok_studio.png")
            return False
        
        # 4. Wait 10 seconds
        self.wait_with_countdown(10, "Waiting after TikTok Studio launch")
        
        # 5. Click on create_grey.png
        self.log_message("Step 5: Searching and clicking on create_grey.png")
        if not self.click_on_image("assets/images/create_grey.png"):
            self.log_message("❌ Failed to click on create_grey.png")
            return False
        
        # 6. Wait 30 seconds
        self.wait_with_countdown(30, "Waiting before publish.py execution")
        
        self.log_message("✅ Preparation sequence completed successfully")
        self.log_message("🚀 Ready for publish.py execution!")
        return True

def main():
    """Main function - just run preparation sequence"""
    print("="*50)
    print("🎬 TIKTOK STUDIO PREPARATION")
    print("="*50)
    print("This script prepares TikTok Studio for post creation:")
    print("1. Click apps.png")
    print("2. Click close_all.png") 
    print("3. Click tiktok_studio.png")
    print("4. Wait 10 seconds")
    print("5. Click create_grey.png")
    print("6. Wait 30 seconds")
    print("="*50)
    
    # Create preparation manager
    prep_manager = PreparationManager()
    
    try:
        # Run preparation sequence
        success = prep_manager.run_preparation_sequence()
        
        if success:
            print("🎉 Preparation completed! Ready for publish.py")
            return 0
        else:
            print("❌ Preparation failed!")
            return 1
            
    except KeyboardInterrupt:
        print("\n⚠️ User interruption (Ctrl+C)")
        return 1
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        return 1

if __name__ == "__main__":
    exit(main())