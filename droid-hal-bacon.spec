# These and other macros are documented in dhd/droid-hal-device.inc
%define device bacon
%define vendor oneplus
%define vendor_pretty OnePlus
%define device_pretty One
%define installable_zip 1
%define enable_kernel_update 1
%define straggler_files \
/selinux_version\
/service_contexts\
%{nil}

%define additional_post_scripts \
/usr/bin/groupadd-user media_rw || :\
%{nil}

%include rpm/dhd/droid-hal-device.inc

