<?php

/**
 * In the world of PHP, occasionally you see inheritance used. This is a very basic
 * exercise to make sure you have a grasp on such a thing
 * 
 * There is a class called Poison, which is defined as follows:
 * 
 * abstract class Poison {
 *   function observe(){
 *     return "Looks drinkable :)";
 *   }
 *   abstract function drink();
 * }
 * 
 * Your job is as follows:
 * 1) Complete the class already started called Beer, and implement the drink
 * function which should return a string
 * 2) Create another class called Wine, which should also extend Poison, and override
 * the observe function to return a different string
 */

/**
 * solution
 */

class Beer extends Poison {
    public function drink() {
        return 'string';
    }
}

class Wine extends Poison {

    public function observe() {
        return 'not drinkable';
    }
    
    public function drink() {
        return 'wine';
    }
}
