#pragma once


#ifdef _WIN32
  #define AFTRBURNER_EXPORT __declspec(dllexport)
#else
  #define AFTRBURNER_EXPORT
#endif

AFTRBURNER_EXPORT void aftrburner();
