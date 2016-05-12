package cheng;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;

public class ListComprehension {
    public static void main(String[] args) throws IOException {
        //list to hold the pokemon
        ArrayList<Pokemon> pokedex = new ArrayList<>();
        //list to hold type strengths
        ArrayList<Strength> strengths = new ArrayList<>();

        //finding read file
        String path = System.getProperty("user.dir") + "/src/";
        System.out.print(path);
        File file = new File(path + "pokemon.txt");

        //load the read file
        BufferedReader buffr = new BufferedReader(new FileReader(file));
        //make a blank line to store the buffer/reader data
        String line;
        //go through the file and load data
        while ((line = buffr.readLine()) != null){
            String temp = line.substring(1, line.length() - 2);
            List<String> pokeList = Arrays.asList(temp.split(","));
            for (int i = 0;i<pokeList.size();i++){
                pokeList.set(i,pokeList.get(i).trim());
            }
            pokeList.get(0);
            Pokemon missingno = new Pokemon(pokeList.get(0),pokeList.get(1),pokeList.get(2),pokeList.get(3));
            pokedex.add(missingno);
        }

        //load the next file
        buffr = new BufferedReader(new FileReader(path + "strength.txt"));
        while ((line = buffr.readLine()) != null){
            String temp = line.substring(1, line.length() - 2);
            List<String> strengthList = Arrays.asList(temp.split(","));
            Strength anon = new Strength(strengthList.get(0),strengthList.get(1),strengthList.get(2), strengthList.get(3), strengthList.get(2));
            strengths.add(anon);
        }

        //print pokemon number 1-10
        System.out.println("SELECT id, name FROM pokedex WHERE id <= 10");
        pokedex.stream()
                .filter(p -> (Integer.parseInt(p.getId()) <= 10))
                .forEach(p -> System.out.println(p.getId() + " " + p.getName()));
            
        //print all grass type pokemon
        System.out.println();
        System.out.println("SELECT id, name FROM pokedex WHERE type1 or type2 == 'Grass'");
        pokedex.stream()
                .filter(p -> (p.getType2().equalsIgnoreCase("Grass")) || (p.getType1().equalsIgnoreCase("Grass")))
                .forEach(p -> System.out.println(p.getId() + " " + p.getName()));

        //group by type 1 and sort the pokemon by name
        System.out.println();
        //SELECT name from pokedex GROUP BY type1 ORDER BY name
        System.out.println("SELECT name from pokedex GROUP BY type1 ORDER BY name");
        pokedex.stream()
                //makes a dictionary {Type1:[p1, p2, etc...],}
                .collect(Collectors.groupingBy(Pokemon::getType1))
                //for each type 1, go through the pokemon list and sort by alpha, then print type1 and sorted list of pokemon names
                .forEach((p1, p2) -> {
                    System.out.println(p1 + ": ");
                    System.out.print("[");
                    p2.sort( (a1, a2) -> a1.getName().compareTo(a2.getName()));
                    p2.stream().forEach(p -> System.out.print(p.getName()+ ", "));
                    System.out.println("]");
                });

        //print all pokemon who are strong against grass type pokemon, grouped by type
        //SELECT name from pokedex where 
        System.out.println();
        System.out.println("print all pokemon who are strong against grass type pokemon");
        String test =  "Grass";
        strengths.stream()
                //form a list of all types that are strong against grass
                .filter(s -> s.getStr1().equalsIgnoreCase(test) || s.getStr2().equalsIgnoreCase(test) || s.getStr3().equalsIgnoreCase(test) || s.getStr4().equalsIgnoreCase(test))
                //for each type found, find pokemon with it
                .forEach(s ->
                {
                    System.out.println(s.getType()+": ");
                    System.out.print("[");
                    pokedex.stream()
                            .filter(p -> p.getType1().equalsIgnoreCase(s.getType()) ||  p.getType2().equalsIgnoreCase(s.getType()))
                            .sorted((p1, p2) -> p1.getName().compareTo(p2.getName()))
                            .forEach(p -> System.out.print(p.getName()+ ", "));
                    System.out.println("]");
                });

//Select name from pokedex
// JOIN strengths where ((strengths.str1) = pokedex.type1) || ((strengths.str1) = pokedex.type2) and where (strengths.str1) = 'Grass' GROUP BY strengths.type 
        SELECT type FROM strengths WHERE str1 = 'Grass' OR str2 = 'Grass' OR str3 = 'Grass' OR str4 = 'Grass' 
        INNER JOIN pokedex ON pokedex.type = strengths.type WHERE  strength.str1 = 'Grass' OR strength.str2 = 'Grass' OR strength.str3 = 'Grass' OR strength.str4 = 'Grass'  
        OR pokedex.type = strengths.type
    }
}