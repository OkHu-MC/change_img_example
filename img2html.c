#include <stdio.h>
#include <string.h>
#include <dirent.h>

void print_files_in_directory(const char *dir_path, FILE *fp) {
    DIR *dir;
    struct dirent *entry;
    char file_path[1024];

    dir = opendir(dir_path);
    if (dir == NULL) {
        perror("Failed to open directory");
        return;
    }

    while ((entry = readdir(dir)) != NULL) {
        if (strstr(entry->d_name, ".jpg") || strstr(entry->d_name, ".png")) {
            sprintf(file_path, "%s/%s", dir_path, entry->d_name);
            fprintf(fp,"<img class=\"image3\" src=\"%s\" alt=\"Example Image\" style=\"position: absolute; top: 0; left: 0;\">",file_path);
    
            printf("%s\n", file_path);
        }
    }

    closedir(dir);
}

int main() {
    const char *directory_path = "./img";
    FILE *fp1,*fp2;
    char ch;
    
    fp1 =fopen("front.txt","r");
    //fread(fp1);


    if ( fp1 == NULL) {
        perror("Error opening source file");
        return -1;
    }

    // 新しいファイルを開く
    fp2 = fopen("pop.html", "w");
    if (fp2 == NULL) {
        perror("Error opening destination file");
        return -2;
    }

    // ファイルから文字を一文字ずつ読み込み、新しいファイルに書き込む
    while ((ch = fgetc(fp1)) != EOF) {
        fputc(ch, fp2);
    }
    fclose(fp1);
    print_files_in_directory(directory_path,fp2);
    //print_files_in_directory();

    fp1 = fopen("end.txt","r");
    if ( fp1 == NULL) {
        perror("Error opening source file");
        return -1;
    }
    // ファイルから文字を一文字ずつ読み込み、新しいファイルに書き込む
    while ((ch = fgetc(fp1)) != EOF) {
        fputc(ch, fp2);
    }
    fclose(fp1);
    
    fclose(fp2);
    
    return 0;
}
