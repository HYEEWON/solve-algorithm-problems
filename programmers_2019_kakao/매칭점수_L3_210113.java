package com.company;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class 매칭점수_L3_210113 {

    public static int solution(String word, String[] pages) {
        word = word.toLowerCase();
        ArrayList<Integer> firstScore = new ArrayList<Integer>();
        ArrayList<Integer> secondScore = new ArrayList<Integer>();
        HashMap<String, ArrayList<String>> links = new HashMap<>();
        Vector<String> urls = new Vector<>();

        for (int i = 0; i < pages.length; ++i) {
            firstScore.add(0);
            secondScore.add(0);
        }

        for (int i = 0; i < pages.length; ++i) {
            String page = pages[i].toLowerCase();
            int count = 0;
            List<String> pageSplit = Arrays.asList(page.split("[^a-zA-Z]"));
            for (String p:pageSplit){
                if (p.equals(word)){
                    count ++;
                }
            }
            firstScore.set(i, count);
            Pattern pattern = Pattern.compile("<meta property=\"og:url\" content=\"https://(\\S+)\"/>");
            Matcher myLink = pattern.matcher(page);
            String url = "";
            while (myLink.find()) {
                url = myLink.group(1);
                urls.add(url);
            }

            pattern = Pattern.compile("<a href=\"https://([\\S]*)\">");
            Matcher outLink = pattern.matcher(page);
            count = 0;
            ArrayList<String> tmp = new ArrayList<>();
            while (outLink.find()){
                String outUrl = outLink.group(1);
                tmp.add(outUrl);
                count++;
            }
            secondScore.set(i, count);
            links.put(url, tmp);
        }
        Vector<Double> finalScore = new Vector<>();
        for (int i = 0; i < pages.length; ++i) {
            double score = 0;
            for (int j = 0; j < pages.length; ++j) {
                if (i != j) {
                    ArrayList<String> tmp = links.get(urls.elementAt(j));
                    for (int k = 0; k < tmp.size(); ++k) {
                        if (tmp.get(k).equals(urls.elementAt(i))) {
                            score += ((double)firstScore.get(j) / secondScore.get(j));
                        }
                    }
                }
            }
            finalScore.add(firstScore.get(i) + score);
        }
        return finalScore.indexOf(Collections.max(finalScore));
    }

    public static int solution2(String word, String[] pages) {
        word = word.toLowerCase();
        ArrayList<Integer> firstScore = new ArrayList<>();
        ArrayList<Integer> secondScore = new ArrayList<>();
        Vector<String> urls = new Vector<>();
        Vector<Double> finalScore = new Vector<>();

        for (int i = 0; i < pages.length; ++i) {
            firstScore.add(0);
            secondScore.add(0);
            finalScore.add(0.0);
        }

        for (int i = 0; i < pages.length; ++i) {
            String page = pages[i].toLowerCase();
            int count = 0;
            List<String> pageSplit = Arrays.asList(page.split("[^a-zA-Z]"));
            for (String p : pageSplit) {
                if (p.equals(word)) {
                    count++;
                }
            }
            firstScore.set(i, count);

            Pattern pattern = Pattern.compile("<meta property=\"og:url\" content=\"https://(\\S+)\"/>");
            Matcher myLink = pattern.matcher(page);
            String url = "";
            while (myLink.find()) {
                url = myLink.group(1);
                urls.add(url);
            }

            pattern = Pattern.compile("<a href=\"https://([\\S]*)\">");
            Matcher outLink = pattern.matcher(page);
            count = 0;
            while (outLink.find()){
                count++;
            }
            secondScore.set(i, count);
        }

        for (int i = 0; i < pages.length; ++i) {
            String page = pages[i].toLowerCase();
            Pattern pattern = Pattern.compile("<a href=\"https://([\\S]*)\">");
            Matcher outLink = pattern.matcher(page);

            while (outLink.find()) {
                String outUrl = outLink.group(1);
                if (urls.contains(outUrl)) {
                    Double score = finalScore.get(urls.indexOf(outUrl));
                    finalScore.set(urls.indexOf(outUrl), score + ((double)firstScore.get(i) / secondScore.get(i)));
                }
            }
            finalScore.set(i, finalScore.get(i)+ firstScore.get(i));
        }
        return finalScore.indexOf(Collections.max(finalScore));
    }

    public static void main(String[] args){
        String word = "Muzi";
        //String[] pages = {"<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"};
        String[] pages = {"<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"};
        System.out.println(solution(word, pages));
    }
}