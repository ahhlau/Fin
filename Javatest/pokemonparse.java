import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;

public class pokemonparse {

    public static ArrayList<Pokemon> pokedex;
    public static ArrayList<Strength> strengths;

    //loads the lists
    public static void loadData() throws IOException{
 //   public static void main(String[] args) throws IOException {
        pokedex = new ArrayList<>();
        //list to hold type strengths
        strengths = new ArrayList<>();

        //finding read file
        String path = System.getProperty("user.dir");
       // System.out.print(path);
        File file = new File(path + "/pokemon");
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
        buffr = new BufferedReader(new FileReader(path + "/strength"));
        while ((line = buffr.readLine()) != null){
            String temp = line.substring(1, line.length() - 2);
            List<String> strengthList = Arrays.asList(temp.split(","));
            for (int i = 0;i<strengthList.size();i++){
                strengthList.set(i,strengthList.get(i).trim());
            }
            Strength anon = new Strength(strengthList.get(0),strengthList.get(1),strengthList.get(2), strengthList.get(3), strengthList.get(4));
            strengths.add(anon);
       // System.out.print(strengths);
        }
    }

    //(exec"import pokemonparse; pokemonsparse.loadData(); pokemonparse.getIDs(['charmander','pidgey']);")
    //input list of pokemon names, get their id's
    public static void getIDs(List<String> pokemon)
    {
        //System.out.println("SELECT id, name FROM pokemon");
        System.out.print("[");
        pokemon.stream()
                //.filter(p -> (p.get()) <= 10))
                .forEach(p ->
                        {
                            String one_poke = p;
                            pokedex.stream()
                                    .filter(p1-> p1.getName().equalsIgnoreCase(one_poke))
                                    .forEach(p1->System.out.print(p1.getId()+", "));
                        }

                );
        System.out.println("]");
    }

    //input type of pokemon, print all pokemon of that type
    public static void getAllofType(String pokemontype)
    {
        pokedex.stream()
                .filter(p -> (p.getType2().equalsIgnoreCase(pokemontype)) || (p.getType1().equalsIgnoreCase(pokemontype)))
                .forEach(p -> System.out.println(p.getId() + " " + p.getName()));

    }

    //input type of pokemon, gets all types that are strong against it
    public static void getStrong(String pokemontype)
    {
        System.out.print("[");
        strengths.stream()
                //form a list of all types that are strong against pokemontype
                .filter(s -> s.getStr1().equalsIgnoreCase(pokemontype) || s.getStr2().equalsIgnoreCase(pokemontype) || s.getStr3().equalsIgnoreCase(pokemontype) || s.getStr4().equalsIgnoreCase(pokemontype))
                .forEach(s -> System.out.print(s.getType() + ", "));
        System.out.println("]");
    }

    //input pokemontype, gets all pokemon that are strong against it, grouped by type1, sorted by name
    public static void getStrongPokemons(String pokemontype)
    {
        strengths.stream()
                //form a list of all types that are strong against pokemontype
                .filter(s -> s.getStr1().equalsIgnoreCase(pokemontype) || s.getStr2().equalsIgnoreCase(pokemontype) || s.getStr3().equalsIgnoreCase(pokemontype) || s.getStr4().equalsIgnoreCase(pokemontype))
                //for each type found, find pokemon with it
                .forEach(s ->
                {
                    System.out.println(s.getType()+": ");
                    System.out.print("[");
                    pokedex.stream()
                            .filter(p -> p.getType1().equalsIgnoreCase(s.getType()))
                            .sorted((p1, p2) -> p1.getName().compareTo(p2.getName()))
                            .forEach(p -> System.out.print(p.getName()+ ", "));
                    System.out.println("]");
                });
    }
}