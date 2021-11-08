#
# This spec file is read by gfortran when linking.
# It is used to specify the libraries we need to link in, in the right
# order.
#

%rename lib liborig
*lib: %{static-liblfortran:--as-needed} -lquadmath %{static-liblfortran:--no-as-needed} -lm %(libgcc) %(liborig)
