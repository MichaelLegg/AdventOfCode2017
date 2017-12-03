#include <stdio.h>

//*
char *input = "86	440	233	83	393	420	228	491	159	13	110	135	97	238	92	396\n\
3646	3952	3430	145	1574	2722	3565	125	3303	843	152	1095	3805	134	3873	3024\n\
2150	257	237	2155	1115	150	502	255	1531	894	2309	1982	2418	206	307	2370\n\
1224	343	1039	126	1221	937	136	1185	1194	1312	1217	929	124	1394	1337	168\n\
1695	2288	224	2667	2483	3528	809	263	2364	514	3457	3180	2916	239	212	3017\n\
827	3521	127	92	2328	3315	1179	3240	695	3144	3139	533	132	82	108	854\n\
1522	2136	1252	1049	207	2821	2484	413	2166	1779	162	2154	158	2811	164	2632\n\
95	579	1586	1700	79	1745	1105	89	1896	798	1511	1308	1674	701	60	2066\n\
1210	325	98	56	1486	1668	64	1601	1934	1384	69	1725	992	619	84	167\n\
4620	2358	2195	4312	168	1606	4050	102	2502	138	135	4175	1477	2277	2226	1286\n\
5912	6261	3393	431	6285	3636	4836	180	6158	6270	209	3662	5545	204	6131	230\n\
170	2056	2123	2220	2275	139	461	810	1429	124	1470	2085	141	1533	1831	518\n\
193	281	2976	3009	626	152	1750	1185	3332	715	1861	186	1768	3396	201	3225\n\
492	1179	154	1497	819	2809	2200	2324	157	2688	1518	168	2767	2369	2583	173\n\
286	2076	243	939	399	451	231	2187	2295	453	1206	2468	2183	230	714	681\n\
3111	2857	2312	3230	149	3082	408	1148	2428	134	147	620	128	157	492	2879\n";
//*/

char *input2 = "5\t9\t2\t8\n\
9\t4\t7\t3\n\
3\t8\t6\t5\n";

int part1(void)
{
        char *input_p   = input;
        char last_char  = 0;
        char cur_char   = 0;
        
        int sum = 0;
        int line_smallest = 99999999999;
        int line_largest = 0;
        
        char buf_num[16];
        char *buf_ptr = buf_num;
        int cur_num = 0;
        
        while((cur_char = *input_p++)) {
                
                *buf_ptr++ = cur_char;
                
                if(cur_char == '\t' || cur_char == '\n') {
                        // null terminate buffer
                        *buf_ptr = 0;
                        
                        cur_num = atoi(buf_num);
                        if (cur_num < line_smallest) {
                                line_smallest = cur_num;
                        }
                        
                        if (cur_num > line_largest) {
                                line_largest = cur_num;
                        }
                        
                        buf_ptr = buf_num;
                }
                
                if (cur_char == '\n') {
                        //printf("Largest: %d Smallest: %d\r\n", line_largest, line_smallest);
                        
                        //printf("Line checksum: %d\r\n\r\n", line_largest - line_smallest);
                        
                        sum += (line_largest - line_smallest);
                        
                        // reset smallest/line_largest
                        line_smallest = 99999999999;
                        line_largest = 0;
                }
        }
        
        return sum;
}

int get_next_num(char **p, int *end)
{
        int num;
        char buf_num[16];
        char *buf_ptr = buf_num;
        char cur_char = **p;
        
        while((cur_char = *(*p)++)) {
                if(isspace(cur_char)) continue;
                
                // null terminate buffer
                *buf_ptr++ = cur_char;
                
                if(**p == '\t' || **p == '\n') {
                        *buf_ptr = 0;
                        num = atoi(buf_num);
                        
                        buf_ptr = buf_num;
                        
                        if(**p == '\n') *end = 1;
                        
                        return num;
                }
        }
        
        return 0;
}

int part2(void)
{
        int sum = 0;
        int end = 0;
        int main_num = 0;
        char *main_num_p = input;
        char *line_start = main_num_p;
        
        printf("%s\r\n", main_num_p);
        
        // Get the next number
        while((main_num = get_next_num(&main_num_p, &end))) {
                char *iter_num_p = line_start;
                int iter_num = 0;
                int iter_end = 0;
                
                printf("Main: %d\r\n", main_num);
                
                while((iter_num = get_next_num(&iter_num_p, &iter_end))) {
                        if(main_num == iter_num) continue;
                        
                        printf("\tComparing %d to %d\r\n", main_num, iter_num);
                        if(main_num % iter_num == 0) {
                                sum += (main_num / iter_num);
                                printf("\t\tFound even! %d\r\n", sum);
                        }
                        
                        if (iter_end == 1) {
                                //printf("End\r\n");
                                iter_end = 0;
                                break;
                        }
                }
                
                if(end) {
                        end = 0;
                        line_start = main_num_p;
                }
        }
        
        return sum;
}

int main(void)
{
        printf("Part1: %d\r\n", part1());
        printf("Part2: %d\r\n", part2());
}



















