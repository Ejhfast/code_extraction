# Global variable from a library not yet initialized when used
%init%{
  LicenseManager::get();
%}
