package com.codewars.flames;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Flames {

	public static String showRelationship(String male, String female){

		String ans = "";
		int i = 0;
		
		String[] flames = {"Friendship","Love","Affection","Marriage","Enemies","Siblings"};
		char[] maleC = male.toCharArray();
		char[] femaleC = female.toCharArray();
		List<Character> common = new ArrayList<Character>();
		List<Character> combined = new ArrayList<Character>();
		
		System.out.println(male);
		System.out.println(female);
		
		for (i = 0; i < maleC.length; i++) {
			for (int j = 0; j < femaleC.length; j++) {
				if(maleC[i] == femaleC[j]){
					common.add(maleC[i]);
				}
			}
		}
		
		for (char c : common){
			for (i = 0; i < maleC.length; i++) {
				if (c == maleC[i]){
					maleC[i] = '\0';
				}
			}
			for (i = 0; i < femaleC.length; i++) {
				if (c == femaleC[i]){
					femaleC[i] = '\0';
				}
			}
		}
		
		for (char c : maleC) {
			if (c != '\0'){
				combined.add(c);
				System.out.println(c);
			}
		}
		
		for (char c : femaleC) {
			if (c != '\0'){
				combined.add(c);
				System.out.println(c);
			}
		}
		
		i = 0;
		
		for (Character character : combined) {
			ans = flames[i];
			i = (i + 1) % 6;
		}
		
		return ans;
	}

}
