package cheng;

public class Strength {
    private String type;
    private String str1;
    private String str2;
    private String str3;
    private String str4;

    public Strength(String type, String str1, String str2, String str3, String str4){
        this.type = type;
        this.str1 = str1;
        this.str2 = str2;
        this.str3 = str3;
        this.str4 = str4;
    }

    public String getType(){return type;}
    public String getStr1(){return str1;}
    public String getStr2(){return str2;}
    public String getStr3(){return str3;}
    public String getStr4(){return str4;}
    public String toString(){return type + " " + str1+ " " + str2 + " "  + str3+ " "+ str4;}

}
