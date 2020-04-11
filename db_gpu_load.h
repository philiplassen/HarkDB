#ifndef DB_GPU_LOAD_H
#define DB_GPU_LOAD_H


#include <vector>
#include <string>

extern "C" {

#include "build/select_where.h"

}

struct context {
	struct futhark_context_config *cfg;
	struct futhark_context *ctx;
};

void create_context(struct context* cont);

void free_context(struct context* cont);

//std::vector<uint32> launchAndExecute(std::vector<std::vector<uint32_t>> db, std::vector<uint64_t> select_cols, struct context* cont);

std::vector<uint32_t> launchAndExecute(uint32_t* db, int* select_cols, int rows, int cols, struct context* cont);

std::vector<uint32_t> launchAndExecute(uint32_t* db, int* select_cols, int rows, int cols);



#endif