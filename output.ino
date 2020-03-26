#include "Keyboard.h"

void typeKey(uint8_t key)
{
  Keyboard.press(key);
  delay(50);
  Keyboard.release(key);
}

/* Init function */
void setup()
{
  // Begining the Keyboard stream
  Keyboard.begin();
  delay(3000);
  Keyboard.press(KEY_LEFT_GUI);

  Keyboard.press('r');

  Keyboard.releaseAll();

  delay(800);

  Keyboard.print(F("notepad"));

  typeKey(KEY_RETURN);

  delay(1800);

  Keyboard.print(F("Hello World!"));
  // Ending stream
  Keyboard.end();
}

/* Unused endless loop */
void loop() {}
