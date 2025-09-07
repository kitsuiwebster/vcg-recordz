import cv2
import pyautogui
import numpy as np
import time
import os
import config  # Import the configuration module
from datetime import datetime

# Function to format time duration
def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f"{int(minutes)}m {seconds:.1f}s"

# Initial pause to switch windows
print("- Preparation... (2 seconds)")
time.sleep(2)

# Start timing overall execution
total_start_time = time.time()

# Generate configuration for this run
run_config = config.generate_run_config()

# Extract variables from the configuration
MODE = run_config["mode"]
NUM_IMAGES = run_config["num_images"]
NUM_TEXTS = run_config["num_texts"]
selected_text_set = run_config["selected_text_set"]
selected_images = run_config["selected_images"]
selected_music_set = run_config["selected_music_set"]
selected_title = run_config["selected_title"]
selected_description = run_config["selected_description"]
selected_hashtags = run_config["selected_hashtags"]
selected_emoji = run_config["selected_emoji"]
emoji_clicks = run_config["emoji_clicks"]
combined_media_set = run_config["combined_media_set"]

print(f"- Using {MODE.upper()} mode with {NUM_IMAGES} images and {NUM_TEXTS} texts")

print(f"- Selected text set: {selected_text_set}")
print(f"- Selected images: {selected_images}")
print(f"- Selected music set: {selected_music_set['spotify']}, {selected_music_set['sound']}")
print(f"- Selected title: {selected_title}")

#################################################
# FUNCTIONS
#################################################

# Function to find and click on an image (keep trying until found)
def click_on_image(image_path, confidence_threshold=0.7, max_attempts=30, wait_time=1):
    attempt = 1
    
    while attempt <= max_attempts:  # Loop with maximum attempts
        print(f"- Attempt {attempt} looking for: {image_path}")
        
        # Take screenshot
        screen = np.array(pyautogui.screenshot())
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
        
        # Load target image
        target = cv2.imread(image_path)
        
        # Check if image was loaded correctly
        if target is None:
            print(f"❌ Could not load image {image_path}")
            return False
        
        # Search for the image
        result = cv2.matchTemplate(screen, target, cv2.TM_CCOEFF_NORMED)
        _, score, _, position = cv2.minMaxLoc(result)
        
        if score > confidence_threshold:  # Confidence threshold
            # Calculate center of image
            h, w = target.shape[:2]
            center_x = position[0] + w//2
            center_y = position[1] + h//2
            
            time.sleep(0.5)
            
            # Click
            pyautogui.click(center_x, center_y)
            print(f"✅ Found and clicked on {image_path} (confidence score: {score:.2f})")
            return True
        else:
            print(f"⚠️ Image not found (best score: {score:.2f})")
            if attempt < max_attempts:
                time.sleep(wait_time)  # Wait before trying again
            attempt += 1
    
    print(f"❌ Failed to find {image_path} after {max_attempts} attempts")
    return False

# Function to scroll down
def scroll_down(start_x=400, start_y=800, end_y=400, duration=0.3):
    print(f"- Scrolling down from ({start_x}, {start_y}) to ({start_x}, {end_y})")
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    pyautogui.moveTo(start_x, end_y, duration=duration)
    pyautogui.mouseUp()
    time.sleep(0.5)  # Short pause after scrolling

def scroll_until_found(image_path, max_scrolls=20, confidence_threshold=0.7):
    print(f"- Scrolling to find: {image_path}")
    
    for i in range(max_scrolls):
        print(f"- Scroll attempt {i+1}/{max_scrolls}")
        
        # Screenshot
        screen = np.array(pyautogui.screenshot())
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
        
        # Load target
        target = cv2.imread(image_path)
        if target is None:
            print(f"❌ Could not load image {image_path}")
            return False
        
        # Match template
        result = cv2.matchTemplate(screen, target, cv2.TM_CCOEFF_NORMED)
        _, score, _, position = cv2.minMaxLoc(result)
        h, w = target.shape[:2]

        print(f"🔍 Best match score: {score:.4f}")
        
        if score > confidence_threshold:
            # Optional: reject matches too dark
            matched_region = screen[position[1]:position[1]+h, position[0]:position[0]+w]
            if np.mean(matched_region) < 30:
                print("⚠️ Match rejected: area too dark (possible false positive)")
                continue

            # Draw rectangle
            top_left = position
            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv2.rectangle(screen, top_left, bottom_right, (0, 255, 0), 2)

            # Click
            center_x = position[0] + w // 2
            center_y = position[1] + h // 2
            pyautogui.click(center_x, center_y)
            print(f"✅ Found and clicked on {image_path} (confidence score: {score:.2f})")
            return True
        
        # Scroll + wait
        scroll_down()
        time.sleep(1.5)  # UI pause

    print(f"❌ Failed to find {image_path} after {max_scrolls} scrolls")
    return False

# Function to handle uppercase characters
def type_with_caps(text):
    caps_on = config.UI_ELEMENTS["caps_on"]
    caps_off = config.UI_ELEMENTS["caps_off"]
    
    i = 0
    while i < len(text):
        if text[i].isupper():
            # Start uppercase sequence
            print("- Found uppercase character, activating caps lock")
            if not click_on_image(caps_on, confidence_threshold=0.6):
                print("❌ Failed to find caps_on button. Typing without caps.")
            time.sleep(0.3)
            if not click_on_image(caps_on, confidence_threshold=0.6):  # Click twice as requested
                print("❌ Failed to find caps_on button second time.")
            time.sleep(0.3)
            
            # Type all consecutive uppercase characters
            uppercase_seq = ""
            while i < len(text) and text[i].isupper():
                uppercase_seq += text[i].lower()  # Type as lowercase since caps is on
                i += 1
            
            print(f"- Typing uppercase sequence: {uppercase_seq}")
            pyautogui.typewrite(uppercase_seq)
            time.sleep(0.3)
            
            # Turn off caps
            print("- Turning off caps lock")
            if not click_on_image(caps_off, confidence_threshold=0.6):
                print("❌ Failed to find caps_off button.")
            time.sleep(0.3)
        else:
            # Type regular character
            pyautogui.typewrite(text[i])
            i += 1
    
    time.sleep(0.5)  # Small pause after typing

# Function to handle special characters
def type_special_char(char):
    key_special_characters = config.UI_ELEMENTS["key_special_characters"]
    key_letters = config.UI_ELEMENTS["key_letters"]
    
    print(f"- Typing special character: {char}")
    
    # Click on special characters key
    if not click_on_image(key_special_characters, confidence_threshold=0.6):
        print("❌ Failed to find special characters key. Typing directly.")
        pyautogui.typewrite(char)
        return
    time.sleep(0.3)
    
    # Click on the specific special character key
    if char == '?':
        key_char = config.UI_ELEMENTS["key_question_mark"]
    elif char == '!':
        key_char = config.UI_ELEMENTS["key_exclamation_mark"]
    elif char == '>':
        key_char = config.UI_ELEMENTS["key_chevron"]
    else:
        print(f"❌ No specific handling for character: {char}")
        pyautogui.typewrite(char)
        return
    
    if not click_on_image(key_char, confidence_threshold=0.6):
        print(f"❌ Failed to find {char} key. Typing directly.")
        pyautogui.typewrite(char)
    time.sleep(0.3)
    
    # Return to letters keyboard
    if not click_on_image(key_letters, confidence_threshold=0.6):
        print("❌ Failed to find letters keyboard key.")
    time.sleep(0.3)

# Function to handle prayer emoji
def type_pray_emoji():
    emojis_button = config.UI_ELEMENTS["emojis_button"]
    emoji_pray = config.UI_ELEMENTS["emoji_pray"]
    keyboard = config.UI_ELEMENTS["keyboard"]
    
    print("- Inserting prayer emoji")
    
    # Click on emojis button
    if not click_on_image(emojis_button, confidence_threshold=0.8):
        print("❌ Failed to find emojis button.")
        return
    time.sleep(0.5)
    
    # Click on prayer emoji
    if not click_on_image(emoji_pray, confidence_threshold=0.6):
        print("❌ Failed to find prayer emoji.")
        return
    time.sleep(0.5)
    
    # Return to keyboard
    if not click_on_image(keyboard, confidence_threshold=0.6):
        print("❌ Failed to find keyboard button.")
        return
    time.sleep(0.5)

# Enhanced typing function to handle all special cases
def type_text(text):
    print(f"- Typing: '{text}'")
    i = 0
    while i < len(text):
        # Check for prayer emoji
        if i < len(text) - 1 and text[i:i+2] == "🙏":
            type_pray_emoji()
            i += 2  # Skip both emoji characters
        # Check for special characters
        elif text[i] in "?!>":
            type_special_char(text[i])
            i += 1
        # Check for uppercase sequences
        elif text[i].isupper():
            # Find the uppercase sequence
            start = i
            while i < len(text) and text[i].isupper():
                i += 1
            uppercase_seq = text[start:i]
            
            print(f"- Typing uppercase sequence: {uppercase_seq}")
            
            # Turn on caps lock
            caps_on = config.UI_ELEMENTS["caps_on"]
            if not click_on_image(caps_on, confidence_threshold=0.6):
                print("❌ Failed to find caps_on button first click.")
            time.sleep(0.3)
            if not click_on_image(caps_on, confidence_threshold=0.6):
                print("❌ Failed to find caps_on button second click.")
            time.sleep(0.3)
            
            # Type each uppercase letter by clicking on its key image
            for letter in uppercase_seq:
                letter_path = f"assets/images/letters/{letter}.png"
                print(f"- Clicking on letter key: {letter_path}")
                
                if not click_on_image(letter_path, confidence_threshold=0.7):
                    print(f"❌ Failed to find image for letter '{letter}'. Typing directly.")
                    pyautogui.typewrite(letter.lower())  # Type lowercase since caps is on
                time.sleep(0.3)
            
            # Turn off caps
            caps_off = config.UI_ELEMENTS["caps_off"]
            if not click_on_image(caps_off, confidence_threshold=0.6):
                print("❌ Failed to find caps_off button.")
            time.sleep(0.3)
        # Regular character
        else:
            pyautogui.typewrite(text[i])
            i += 1
    
    time.sleep(0.5)

def scroll_down_lower(start_x=400, start_y=900, end_y=700, duration=0.3):
    print(f"- Scrolling down from ({start_x}, {start_y}) to ({start_x}, {end_y})")
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    pyautogui.moveTo(start_x, end_y, duration=duration)
    pyautogui.mouseUp()
    time.sleep(0.5)

def swipe_left(start_x=450, end_x=70, y_pos=200 , duration=0.8):
    print(f"- Swiping left from ({start_x}, {y_pos}) to ({end_x}, {y_pos})")
    pyautogui.moveTo(start_x, y_pos)
    time.sleep(0.2)
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.moveTo(end_x, y_pos, duration=duration)
    pyautogui.mouseUp()
    time.sleep(0.5)
    
def swipe_right(start_x=70, end_x=500, y_pos=350, duration=0.8):
    print(f"- Swiping right from ({start_x}, {y_pos}) to ({end_x}, {y_pos})")
    pyautogui.moveTo(start_x, y_pos)
    time.sleep(0.2)
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.moveTo(end_x, y_pos, duration=duration)
    pyautogui.mouseUp()
    time.sleep(0.5)

# Function to find multiple images in the current screen
def find_images_in_current_screen(image_paths, confidence_threshold=0.5):
    print("- Scanning current screen for all required images")
    
    # Take screenshot
    screen = np.array(pyautogui.screenshot())
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    
    found_images = []
    
    for img_path in image_paths:
        # Load target image
        target = cv2.imread(img_path)
        
        # Check if image was loaded correctly
        if target is None:
            print(f"❌ Could not load image {img_path}")
            continue
        
        # Search for the image
        result = cv2.matchTemplate(screen, target, cv2.TM_CCOEFF_NORMED)
        _, score, _, position = cv2.minMaxLoc(result)
        
        # Only consider as found if score is above threshold
        if score > confidence_threshold:
            # Optional validation: Check if the image is fully visible
            h, w = target.shape[:2]
            screen_h, screen_w = screen.shape[:2]
            
            # Check if the image is completely within the screen bounds
            if (position[0] >= 0 and position[1] >= 0 and 
                position[0] + w <= screen_w and position[1] + h <= screen_h):
                print(f"✅ Found image {img_path} (score: {score:.2f})")
                found_images.append((img_path, position, score, target.shape))
            else:
                print(f"⚠️ Image {img_path} partially off-screen, skipping (score: {score:.2f})")
    
    # Sort found images by confidence score (highest first)
    found_images.sort(key=lambda x: x[2], reverse=True)
    
    return found_images

# New function to batch process images with direct clicking
def batch_process_images(image_paths, max_scroll_attempts=20, confidence_threshold=0.5):
    print("\n- Starting batch image processing")
    remaining_images = set(image_paths)
    processed_images = set()
    scroll_count = 0
    
    select_button = config.UI_ELEMENTS["select_button"]
    back_button = config.UI_ELEMENTS["back_button"]
    
    while remaining_images and scroll_count <= max_scroll_attempts:
        # Find all visible images in the current screen
        found_images = find_images_in_current_screen(list(remaining_images), confidence_threshold)
        
        if found_images:
            print(f"- Found {len(found_images)} images in current screen")
            
            # Process each found image
            for img_info in found_images:
                img_path, position, score, shape = img_info
                
                # Only process if it's still in the remaining set
                if img_path in remaining_images:
                    print(f"- Processing found image: {img_path} (score: {score:.2f})")
                    
                    # Calculate center coordinates of the found image
                    h, w = shape[:2]
                    center_x = position[0] + w // 2
                    center_y = position[1] + h // 2
                    
                    # Click directly on the found image position
                    print(f"- Clicking directly at position ({center_x}, {center_y})")
                    pyautogui.click(center_x, center_y)
                    time.sleep(0.5)
                    
                    # Now click on select button
                    if not click_on_image(select_button, confidence_threshold=0.6):
                        print(f"❌ Failed to find select button for {img_path}. Skipping.")
                        continue
                    time.sleep(0.5)
                    
                    # Click on back button
                    if not click_on_image(back_button, confidence_threshold=0.75):
                        print(f"❌ Failed to find back button after selecting {img_path}. Continuing anyway.")
                    time.sleep(0.5)
                    
                    # Mark as processed
                    remaining_images.remove(img_path)
                    processed_images.add(img_path)
                    print(f"✅ Successfully processed {img_path}")
        
        # If we've processed all images or reached max scrolls, exit the loop
        if not remaining_images or scroll_count >= max_scroll_attempts:
            break
        
        # Scroll down to look for more images
        print(f"- Scrolling down to find remaining {len(remaining_images)} images")
        scroll_down()
        time.sleep(1.5)  # Wait for screen to update
        scroll_count += 1
    
    # Report results
    print(f"\n- Batch processing completed:")
    print(f"  ✅ Successfully processed {len(processed_images)}/{len(image_paths)} images")
    print(f"  ⚠️ Failed to find {len(remaining_images)}/{len(image_paths)} images")
    
    if remaining_images:
        print(f"  Missing images: {', '.join(remaining_images)}")
    
    return processed_images, remaining_images

#################################################
# PART 1: Initial setup and media selection
#################################################

print("\n--- PART 1: Starting initial TikTok post setup and media selection ---\n")
part1_start_time = time.time()

# TikTok post automation flow - First two buttons
first_button = config.UI_ELEMENTS["create_button"]
second_button = config.UI_ELEMENTS["upload_button"]

# Click on create button (keep trying until found)
print(f"- Starting search for first button: {first_button}")
if not click_on_image(first_button):
    print("❌ Failed to find create button. Aborting.")
    exit(1)

# Wait a bit after successful click
time.sleep(0.5)

# Click on upload button (keep trying until found)
print(f"- Starting search for second button: {second_button}")
if not click_on_image(second_button):
    print("❌ Failed to find upload button. Aborting.")
    exit(1)

print("- Initial step of TikTok post automation completed")

# Continue with the new flow
print("- Continuing with media selection flow")

# Click on 'all.png'
all_button = config.UI_ELEMENTS["all_button"]
print(f"- Looking for {all_button}")
if not click_on_image(all_button):
    print("❌ Failed to find 'all' button. Aborting.")
    exit(1)
time.sleep(0.5)

# Scroll to find and click on 'madpoof.png'
madpoof_button = config.UI_ELEMENTS["madpoof_button"]
print(f"- Scrolling to find {madpoof_button}")
if not scroll_until_found(madpoof_button, max_scrolls=30, confidence_threshold=0.7):
    print("❌ Failed to find 'madpoof' button after scrolling. Aborting.")
    exit(1)
time.sleep(0.5)

# Process the poof images as a batch
poof_images = combined_media_set[:NUM_IMAGES]  # First NUM_IMAGES are poof images
print(f"- Attempting to batch process {NUM_IMAGES} poof images")

# Try processing with gradually decreasing confidence thresholds if needed
thresholds = [0.7, 0.55, 0.4]
for threshold in thresholds:
    print(f"- Trying with confidence threshold: {threshold}")
    processed_images, remaining_images = batch_process_images(list(set(poof_images)), max_scroll_attempts=20, confidence_threshold=threshold)
    
    # If we've processed all images, break out of the loop
    if not remaining_images:
        print(f"- All images processed successfully with threshold {threshold}")
        break
    
    # If there are still remaining images but we're not on the last threshold, 
    # remove the processed images from poof_images for the next attempt
    if remaining_images and threshold != thresholds[-1]:
        poof_images = list(remaining_images)  # Only keep the ones we still need to find
    
    # If there are still remaining images but we're on the last threshold, continue anyway
    if threshold == thresholds[-1] and remaining_images:
        print(f"⚠️ Could not find all images even with lowest threshold. Missing: {len(remaining_images)}/{NUM_IMAGES}")
        
# Report how many images were processed
processed_count = NUM_IMAGES - len(remaining_images) if 'remaining_images' in locals() else 0
print(f"- {processed_count}/{NUM_IMAGES} poof images were successfully processed")


madpoof_2_button = config.UI_ELEMENTS["madpoof_2_button"]
print(f"- Looking for {madpoof_2_button}")
if not click_on_image(madpoof_2_button):
    print("❌ Failed to find 'madpoof_2' button. Aborting.")
    exit(1)
time.sleep(0.5)

# NEW: Scroll to find and click on 'covers.png'
covers_button = config.UI_ELEMENTS["covers_button"]
print(f"- Scrolling to find {covers_button}")
if not scroll_until_found(covers_button, max_scrolls=30, confidence_threshold=0.7):
    print("❌ Failed to find 'covers' button after scrolling. Aborting.")
    exit(1)
time.sleep(0.5)

if MODE != "medium":
    # NOW: Scroll to find and select the Spotify image
    spotify_image = combined_media_set[NUM_IMAGES]
    spotify_confidence = selected_music_set.get("spotify_confidence", 0.5)

    print(f"- Scrolling to find Spotify image: {spotify_image} (confidence threshold: {spotify_confidence})")

    found_spotify = False
    for i in range(20):  # Max 20 scroll attempts
        print(f"- Scroll attempt {i+1}/20")
        
        # Take screenshot
        screen = np.array(pyautogui.screenshot())
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
        
        # Load target image
        target = cv2.imread(spotify_image)
        
        # Check if image was loaded correctly
        if target is None:
            print(f"❌ Could not load image {spotify_image}")
            break
        
        # Search for the image
        result = cv2.matchTemplate(screen, target, cv2.TM_CCOEFF_NORMED)
        _, score, _, position = cv2.minMaxLoc(result)
        
        print(f"🔍 Best match score: {score:.4f} (threshold: {spotify_confidence})")
        
        if score > spotify_confidence:
            found_spotify = True
            h, w = target.shape[:2]
            center_x = position[0] + w // 2
            center_y = position[1] + h // 2
            
            # Click directly on the found position
            print(f"- Clicking directly at position ({center_x}, {center_y})")
            pyautogui.click(center_x, center_y)
            time.sleep(0.5)
            
            # Now click on select button
            select_button = config.UI_ELEMENTS["select_button"]
            if not click_on_image(select_button, confidence_threshold=0.6):
                print(f"❌ Failed to find select button for Spotify image. Continuing anyway.")
            else:
                time.sleep(0.5)
                
                # Click on back button
                back_button = config.UI_ELEMENTS["back_button"]
                if not click_on_image(back_button, confidence_threshold=0.75):
                    print(f"❌ Failed to find back button after selecting Spotify image. Continuing anyway.")
                time.sleep(0.5)
                
            print(f"✅ Successfully processed Spotify image")
            break
        
        # Image not found, scroll down and try again
        scroll_down()
        time.sleep(1.5)  # UI pause

    if not found_spotify:
        print("❌ Failed to find Spotify image after multiple scrolls. Continuing anyway.")

else:
    print(f"- Mode {MODE}: Skipping Spotify image processing")
    
# Click on next.png
next_button = config.UI_ELEMENTS["next_button"]
print(f"- Looking for {next_button}")
if not click_on_image(next_button):
    print("❌ Failed to find 'next' button. Aborting.")
    exit(1)

part1_end_time = time.time()
part1_duration = part1_end_time - part1_start_time
print(f"\n✅ Part 1 completed in {format_time(part1_duration)}")
print("- First part of TikTok automation completed, continuing with sound and text...")

#################################################
# PART 2: Sound and text configuration
#################################################

print("\n--- PART 2: Starting sound and text configuration ---\n")
part2_start_time = time.time()

# Click on music_notes.png
music_notes_button = config.UI_ELEMENTS["music_notes_button"]
print(f"- Looking for {music_notes_button}")
if not click_on_image(music_notes_button, confidence_threshold=0.8):  # Lowered confidence threshold
    print("❌ Failed to find 'music_notes' button. Aborting.")
    exit(1)
time.sleep(2)  # Increased wait time to ensure UI updates

# Click on favorites.png
favorites_button = config.UI_ELEMENTS["favorites_button"]
print(f"- Looking for {favorites_button}")
if not click_on_image(favorites_button):
    print("❌ Failed to find 'favorites' button. Aborting.")
    exit(1)
time.sleep(0.5)

# Scroll until finding the sound that matches our selected set
if MODE == "medium":
    sound_image = combined_media_set[NUM_IMAGES]
else:
    sound_image = combined_media_set[NUM_IMAGES + 1]

sound_confidence = selected_music_set.get("sound_confidence", 0.8)

print(f"- Scrolling to find {sound_image} (confidence threshold: {sound_confidence})")

# Scroll until finding the sound
found_sound = False
for i in range(20):  # Max 20 scroll attempts
    print(f"- Scroll attempt {i+1}/20")
    
    # Take screenshot
    screen = np.array(pyautogui.screenshot())
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    
    # Load target image
    target = cv2.imread(sound_image)
    
    # Check if image was loaded correctly
    if target is None:
        print(f"❌ Could not load image {sound_image}")
        break
    
    # Search for the image
    result = cv2.matchTemplate(screen, target, cv2.TM_CCOEFF_NORMED)
    _, score, _, position = cv2.minMaxLoc(result)
    
    print(f"🔍 Best match score: {score:.4f}")
    
    if score > sound_confidence:
        found_sound = True
        h, w = target.shape[:2]
        center_x = position[0] + w // 2
        center_y = position[1] + h // 2
        pyautogui.click(center_x, center_y)
        time.sleep(5)
        print(f"✅ Found and clicked sound at ({center_x}, {center_y}) (score: {score:.2f})")
        break
    
    # Image not found, scroll down and try again
    scroll_down_lower()  # Using the new scroll function with lower starting position
    time.sleep(1.5)  # UI pause

# Click on specific coordinates after finding the sound
if found_sound:
    print("- Clicking at position (400, 400)")
    pyautogui.click(400, 400)
    time.sleep(0.5)

# Process each text in the selected text set (either 4 or 10 texts)
current_text_index = 0

# Function to handle each text card
def process_text_card(text_content, is_first_card=False):
    global current_text_index
    
    # Only do the initial swipes for the very first text card
    if is_first_card:
        print("- Swiping right 2 times before looking for text button (first card only)")
        swipe_right()
        time.sleep(0.5)
        swipe_right()
        time.sleep(0.5)
    
    # Click on text.png
    text_button = config.UI_ELEMENTS["text_button"]
    print(f"- Looking for {text_button} for text card {current_text_index + 1}")
    if not click_on_image(text_button):
        print(f"❌ Failed to find 'text' button for card {current_text_index + 1}. Aborting.")
        return False
    time.sleep(0.5)
    
    # Check if the text contains line breaks
    if '\n' in text_content:
        # Split the text into lines
        lines = text_content.split('\n')
        
        # Type only the first line
        first_line = lines[0]
        print(f"- Typing first line: '{first_line}'")
        
        # Handle prayer emoji in the first line
        if "🙏" in first_line:
            segments = first_line.split("🙏")
            
            # Type first segment
            if segments[0]:
                type_text(segments[0])
            
            # Insert prayer emoji
            type_pray_emoji()
            
            # Type remaining segments with prayer emoji between them
            for segment in segments[1:]:
                if segment:
                    type_text(segment)
        else:
            # Type regular text with special character handling
            type_text(first_line)
        
        time.sleep(0.5)
        
        # For each additional line, add a line break and then type the line
        for i in range(1, len(lines)):
            # Click on break.png to add a line break
            break_button = config.UI_ELEMENTS["break_button"]
            print(f"- Looking for {break_button} for line {i+1}")
            if not click_on_image(break_button):
                print(f"❌ Failed to find 'break' button for line {i+1}. Continuing without line break.")
                break
            time.sleep(0.5)
            
            # Type the current line
            current_line = lines[i]
            print(f"- Typing line {i+1}: '{current_line}'")
            
            # Handle prayer emoji in this line
            if "🙏" in current_line:
                segments = current_line.split("🙏")
                
                # Type first segment
                if segments[0]:
                    type_text(segments[0])
                
                # Insert prayer emoji
                type_pray_emoji()
                
                # Type remaining segments with prayer emoji between them
                for segment in segments[1:]:
                    if segment:
                        type_text(segment)
            else:
                # Type regular text with special character handling
                type_text(current_line)
            
            time.sleep(0.5)
    else:
        # For single-line text, handle prayer emoji
        if "🙏" in text_content:
            segments = text_content.split("🙏")
            
            # Type first segment
            if segments[0]:
                type_text(segments[0])
            
            # Insert prayer emoji
            type_pray_emoji()
            
            # Type remaining segments with prayer emoji between them
            for segment in segments[1:]:
                if segment:
                    type_text(segment)
        else:
            # Type regular text with special character handling
            type_text(text_content)
    
    # For the first text, add contour and adjust size
    if current_text_index == 0:
        # Click on contour.png
        contour_button = config.UI_ELEMENTS["contour_button"]
        print(f"- Looking for {contour_button}")
        if not click_on_image(contour_button, confidence_threshold=0.5):
            print("❌ Failed to find 'contour' button. Continuing anyway.")
        
        # Click on size.png and move 50 pixels up
        size_button = config.UI_ELEMENTS["size_button"]
        print(f"- Looking for {size_button}")
        if click_on_image(size_button, confidence_threshold=0.8):
            # Get current mouse position
            current_pos = pyautogui.position()
            # Press and hold
            pyautogui.mouseDown()
            # Move 50 pixels up
            pyautogui.moveTo(current_pos.x, current_pos.y - 50, duration=0.3)
            # Release
            pyautogui.mouseUp()
            print("✅ Size adjusted")
            time.sleep(0.5)
    
    # Click done when finished with this text card
    done_button = config.UI_ELEMENTS["done_black_button"]
    print(f"- Looking for {done_button}")
    if not click_on_image(done_button, confidence_threshold=0.7):
        print(f"❌ Failed to find 'done' button for card {current_text_index + 1}. Aborting.")
        return False
    time.sleep(0.5)
    
    # Only swipe left if this is NOT the last card
    # We'll handle this logic in the main loop
    current_text_index += 1
    return True

# Track time for text processing
text_start_time = time.time()

# Process all text cards with corrected swipe logic
for i, text in enumerate(selected_text_set):
    is_first_card = (i == 0)  # Only the first card gets the initial right swipes
    is_last_card = (i == len(selected_text_set) - 1)  # Check if this is the last card
    
    if not process_text_card(text, is_first_card):
        print("❌ Error processing text cards. Attempting to continue.")
        break
    
    # Swipe left to the next card ONLY if this is not the last card
    if not is_last_card:
        swipe_left()
        time.sleep(0.5)
        
text_end_time = time.time()     
text_duration = text_end_time - text_start_time
print(f"- Text processing completed in {format_time(text_duration)}")

# Click on next.png after all text cards are done
next_button = config.UI_ELEMENTS["next_button"]
print(f"- Looking for final {next_button}")
if not click_on_image(next_button):
    print("❌ Failed to find final 'next' button. Aborting.")
    exit(1)

part2_end_time = time.time()
part2_duration = part2_end_time - part2_start_time
print(f"\n✅ Part 2 completed in {format_time(part2_duration)}")

#################################################
# PART 3: Description, hashtags, emojis, and saving to drafts
#################################################

print("\n--- PART 3: Starting description, hashtags, emojis, and saving to drafts ---\n")
part3_start_time = time.time()

# 1. Click on description.png
description_button = config.UI_ELEMENTS["description_button"]
print(f"- Looking for {description_button}")
if not click_on_image(description_button, confidence_threshold=0.6):
    print("❌ Failed to find 'description' button. Aborting.")
    exit(1)
time.sleep(1)  # Longer pause to ensure the input field is ready

# Type the selected description with special character handling
print(f"- Selected description to type: {selected_description}")
type_text(selected_description)
time.sleep(0.5)

# Check if we need to do the special collaborator flow BEFORE hashtags
spotify_filename = os.path.basename(selected_music_set["spotify"])
collaborator_prefixes = ["gaxve", "shidozz", "cxmet", "oddgyes"]
needs_collaborator_flow = any(spotify_filename.lower().startswith(prefix) for prefix in collaborator_prefixes)

if needs_collaborator_flow:
    print(f"- Detected collaborator in filename: {spotify_filename}")
    print("- Executing special collaborator flow in description...")
    
    type_text(" ")
    time.sleep(0.5)
    
    # Navigate to emoji section
    home_button = config.UI_ELEMENTS["home_button"]
    print(f"- Looking for {home_button}")
    if not click_on_image(home_button, confidence_threshold=0.7):
        print("❌ Failed to find 'home' button. Attempting to continue...")
    time.sleep(1)

    tiktok_studio_button = config.UI_ELEMENTS["tiktok_studio_button"]
    print(f"- Looking for {tiktok_studio_button}")
    if not click_on_image(tiktok_studio_button, confidence_threshold=0.7):
        print("❌ Failed to find 'tiktok_studio' button. Attempting to continue...")
    time.sleep(1)

    # Click on emojis.png
    emojis_button = config.UI_ELEMENTS["emojis_button"]
    print(f"- Looking for {emojis_button}")
    if not click_on_image(emojis_button, confidence_threshold=0.8):
        print("❌ Failed to find 'emojis' button. Continuing anyway...")
    else:
        time.sleep(1)
        
        # Click on emoji_heart.png
        emoji_heart = config.UI_ELEMENTS["emoji_heart"]
        print(f"- Looking for {emoji_heart}")
        if not click_on_image(emoji_heart, confidence_threshold=0.8):
            print("❌ Failed to find 'emoji_heart' button. Continuing anyway...")
        time.sleep(0.5)
        
        # Click on mention.png
        mention_button = config.UI_ELEMENTS["mention"]
        print(f"- Looking for {mention_button}")
        if not click_on_image(mention_button, confidence_threshold=0.8):
            print("❌ Failed to find 'mention' button. Continuing anyway...")
        time.sleep(1)
        
        # Determine which collaborator to click based on filename
        collaborator_button = None
        for prefix in collaborator_prefixes:
            if spotify_filename.lower().startswith(prefix):
                collaborator_button = config.UI_ELEMENTS[prefix]
                print(f"- Looking for collaborator button: {collaborator_button}")
                break
        
        if collaborator_button:
            if not click_on_image(collaborator_button, confidence_threshold=0.8):
                print(f"❌ Failed to find collaborator button {collaborator_button}. Continuing anyway...")
            time.sleep(1)

time.sleep(0.5)

# Click on hashtags.png before starting hashtags
hashtags_button = config.UI_ELEMENTS["hashtags"]
print(f"- Looking for {hashtags_button}")
if not click_on_image(hashtags_button, confidence_threshold=0.6):
    print("❌ Failed to find 'hashtags' button. Continuing anyway...")
time.sleep(0.5)

# Click on back button to exit hashtags mode
key_back = config.UI_ELEMENTS["key_back"]
print(f"- Looking for {key_back}")
if not click_on_image(key_back, confidence_threshold=0.6):
    print("❌ Failed to find 'key_back' button. Continuing anyway...")
time.sleep(0.5)

# Click on special characters key once at the beginning
key_special_characters = config.UI_ELEMENTS["key_special_characters"]
key_hashtag = config.UI_ELEMENTS["key_hashtag"]

print(f"- Looking for special characters key")
if not click_on_image(key_special_characters, confidence_threshold=0.6):
    print("❌ Failed to find special characters key. Aborting hashtags.")
else:
    time.sleep(0.5)
    
    # For each hashtag, click on hashtag key, then type the tag
    for i, hashtag in enumerate(selected_hashtags):
        print(f"- Typing hashtag {i+1}/5: {hashtag}")
        
        # Click on hashtag key
        print(f"- Looking for hashtag key")
        if not click_on_image(key_hashtag, confidence_threshold=0.6):
            print("❌ Failed to find hashtag key. Typing # manually...")
            type_text("#")
            time.sleep(0.5)
            # Type the hashtag text (without #)
            type_text(hashtag)
        else:
            time.sleep(0.5)
            # Type the hashtag text (without #) - le # a été tapé par le bouton
            type_text(hashtag)
        time.sleep(0.5)
        
        # Add space between hashtags (except for the last one)
        if i < len(selected_hashtags) - 1:
            type_text(" ")
            time.sleep(0.3)

time.sleep(1)

# 3. Click on title.png
title_button = config.UI_ELEMENTS["title_button"]
print(f"- Looking for {title_button}")
if not click_on_image(title_button, confidence_threshold=0.6):
    print("❌ Failed to find 'title' button. Aborting.")
    exit(1)
time.sleep(1)

# Type the selected title for this track with special character handling
print(f"- Selected title: {selected_title}")
type_text(selected_title)
time.sleep(0.5)

# Navigate to emoji section
home_button = config.UI_ELEMENTS["home_button"]
print(f"- Looking for {home_button}")
if not click_on_image(home_button, confidence_threshold=0.7):
    print("❌ Failed to find 'home' button. Attempting to continue...")
time.sleep(1)

tiktok_studio_button = config.UI_ELEMENTS["tiktok_studio_button"]
print(f"- Looking for {tiktok_studio_button}")
if not click_on_image(tiktok_studio_button, confidence_threshold=0.7):
    print("❌ Failed to find 'tiktok_studio' button. Attempting to continue...")
time.sleep(1)

# 4. Click on emojis.png (standard flow for final emoji reactions)
emojis_button = config.UI_ELEMENTS["emojis_button"]
print(f"- Looking for {emojis_button}")
if not click_on_image(emojis_button, confidence_threshold=0.9):
    print("❌ Failed to find 'emojis' button. Aborting.")
    exit(1)
time.sleep(1)

# Track emoji time
emoji_start_time = time.time()

# 5. Click on the selected emoji the random number of times
for i in range(emoji_clicks):
    print(f"- Emoji click {i+1}/{emoji_clicks}")
    if not click_on_image(selected_emoji, confidence_threshold=0.8):
        print(f"❌ Failed to find emoji on attempt {i+1}. Continuing with next...")
        # Try once more with a longer wait
        time.sleep(1)
        if not click_on_image(selected_emoji, confidence_threshold=0.6):
            print("❌ Still couldn't find emoji. Moving on...")
            break
    time.sleep(0.3)  # Short pause between clicks

emoji_end_time = time.time()
emoji_duration = emoji_end_time - emoji_start_time
print(f"- Emoji clicking completed in {format_time(emoji_duration)}")

# 6. Click on done_white.png
done_white_button = config.UI_ELEMENTS["done_white_button"]
print(f"- Looking for {done_white_button}")
if not click_on_image(done_white_button, confidence_threshold=0.6):
    # Try with done_black as a fallback
    done_black_button = config.UI_ELEMENTS["done_black_button"]
    print(f"- Trying fallback: {done_black_button}")
    if not click_on_image(done_black_button, confidence_threshold=0.6):
        print("❌ Failed to find 'done' button. Aborting.")
        exit(1)
time.sleep(1)

# 7. Click on drafts.png
drafts_button = config.UI_ELEMENTS["drafts_button"]
print(f"- Looking for {drafts_button}")
if not click_on_image(drafts_button, confidence_threshold=0.6):
    print("❌ Failed to find 'drafts' button. Aborting.")
    exit(1)

part3_end_time = time.time()
part3_duration = part3_end_time - part3_start_time
print(f"\n✅ Part 3 completed in {format_time(part3_duration)}")

# Calculate total time
total_end_time = time.time()
total_duration = total_end_time - total_start_time

# Print timing summary
print("\n--------------------------------------------------")
print("⏱️ TIMING SUMMARY")
print("--------------------------------------------------")
print(f"Part 1 (Setup & Media): {format_time(part1_duration)}")
print(f"Part 2 (Sound & Text): {format_time(part2_duration)}")
print(f"Part 3 (Description & Finalization): {format_time(part3_duration)}")
print(f"Total execution time: {format_time(total_duration)}")
print("--------------------------------------------------")

print("\n✅ Complete TikTok post automation flow completed successfully!")
print("✅ Post has been saved to drafts")