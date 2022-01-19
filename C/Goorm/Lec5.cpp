#include <stdio.h>

typedef struct
{
	char name[30];
	int kor; // 국어
	int eng; // 영어
	int math; // 수학
	float avg; // 평균
} Student;

int main()
{
	Student s[3];
	
	for(int i=0; i<3; i++)
	{
		scanf("%s ", s[i].name);
		scanf("%d", &s[i].kor);
		scanf("%d", &s[i].eng);
		scanf("%d", &s[i].math);
		s[i].avg = (s[i].kor+s[i].eng+s[i].math)/3.0f;
	}

	for(int i=0; i<3; i++)
	{
		printf("%s ", s[i].name);
		printf("%.1f\n", s[i].avg);
	}
	
	return 0;
}