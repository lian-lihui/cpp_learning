
import sys
import scipy.signal as SIG
import numpy as NP

def AlexNet_test( ):
    sys.stdout.write( "This is inside singleLayer\n" )

# ---------------------------------------------------------------------------- 
#   Convolution
# ---------------------------------------------------------------------------- 
def AlexNet_conv1( inputData, kernelSet, padding = False, crossGroup = False ):
    """ Do AlexNet convolution:
        inputData: [ #group, height, width, #channel ]
        kernelSet: [ #group, #kernel per group, kernel_height, kernel_width, #channel ] 
        """

    #1. Check input shape
    if len( inputData.shape ) != 4:
        sys.stderr.write( "Error: inputData should be 4 dimentional, actual=%d\n" %
               len( inputData.shape ) )
        sys.exit( 1 )

    if len( kernelSet.shape ) != 5: 
        sys.stderr.write( "Error: kernelData should be 5 dimentional\n" )
        sys.exit( 1 )

    ( inputGroup, inputHeight, inputWidth, inputChannel ) = inputData.shape
    ( kernelGroup, numKernelPerGroup, kernelHeight, kernelWidth, kernelChannel ) = kernelSet.shape
    if inputChannel != kernelChannel:
        sys.stderr.write( "Error: Channel size differs between inputData and kernelSet\n" )
        sys.exit( 1 )
 
    #2. Do convolution 
    resultHeight = inputHeight
    resultWidth  = inputWidth
    if not padding:
        resultHeight = inputHeight - kernelSet   + 1
        resultWidth  = inputWidth  - kernelWidth + 1

    if crossGroup:
        convResult_final = NP.empty( [],
                (0, numKernelPerGroup, resultHeight, resultWidth, inputChannel) )
                

        for inputGroupIter in range( inputGroup ):
            for kernelGroupIter in range( kernelGroup ):
                convResult_2 = NP.empty( (numKernelPerGroup, resultHeight, resultWidth, 0),
                        dtype=NP.float16 )

                for channelIter in range( inputChannel ):
                    singleInput = inputData[inputGroupIter, :, :, channelIter]

                    convResult_1 = NP.epmty( ( 0, resultHeight, resultWidth), dtype=NP.float16 )
                    for kernelIter in range( numKernelPerGroup ):
                        kernel = kernelData[kernelGroupIter, kernelIter, :, :, channelIter]
                        if padding:
                            convResult = SIG.convolve2d( singleInput, kernel, mode='full',
                                    boundary='fill', fillValue = 0 )
                            convResult_1 = NP.append( convResult_1, convResult, axis = 0 )
                        else:
                            convResult = SIG.convolve2d( singleInput, kernel, mode='valid' )
                            convResult_1 = NP.append( convResult_1, convResult, axis = 0 )
                    convResult_2 = NP.append( convResult_2, convResult_1[:,:,:, NP.newaxis], axis=-1 )
                convResult_final = NP.append( convResult_final,
                        convResult_2[NP.newaxis, ], axis = 0 )
        return convResult_final

    else:
        if inputGroup != kernelGroup:
            sys.stderr.write( "Error: #of groups are different in inputData and kernelSet\n" )
            sys.exit( 1 )

        convResult_final = numpy.array( [], dtype=NP.float16 )
        convResult_final.reshape( [inputGroup, resultHeight, resultWidth, inputChannel] )

        for groupIter in range( inputGroup ): 
            convResult_2 = numpy.array( [], dtype=NP.float16 )
            convResult_2.reshape( [resultHeight, resultWidth, inputChannel] )
            for channelIter in range( inputChannel ):
                singleInput = inputData[groupIter, :, :, channelIter]
                convResult_1 = numpy.array( [], dtype=NP.float16 )
                convResult_1.reshape( [resultHeight, resultWidth] )

                for kernelIter in range( numKernelPerGroup ):
                    kernel = kernelData[groupIer, kernelIter, :, :, channelIter]
                    if padding:
                        convResult = SIG.convolve2d( singleInput, kernel, model='full', boundary='fill', fillVale = 0 )
                        convResult_1 = NP.stack( convResult_1, convResult, axis = 0 )
                    else:
                        convResult = SIG.convolve2d( singleInput, kernel, model='valid' )
                        convResult_1 = NP.stack( convResult_1, convResult, axis = 0 )
                convResult_2 = NP.stack( convResult_2, convResult_1, axis = -1 )
        convResult_final = NP.stack( convResult_final, convResult_2, axis = 0 )
        return convResult_final


# ---------------------------------------------------------------------------------------------------------
#    Full connection layer
# ---------------------------------------------------------------------------------------------------------
def AlexNet_fc( inputData, weight ):
    """ input: 1-D vector
        weight: 2-D array"""

    if len( inputData.shape ) != 1:
        sys.stderr.write( "Error: full connection layer, input should be a 1-D vector!\n" )
        sys.exit( 1 )

    if len( weight.shape ) != 2:
        sys.stderr.write( "Error: full connection layer, weight should be a 2-D matrix!\n" )
        sys.exit( 1 )

    if inputData.shape[0] != weight.shape[1]:
        sys.stderr.write( "Error: matix and vector size doesn't match!\n" )
        sys.exit( 1 )

    mat = NP.asmatrix( weight )
    return (mat * inputData).getA( )



# ---------------------------------------------------------------------------------------------------------
#    ReLU
# ---------------------------------------------------------------------------------------------------------
def AlexNet_ReLU( inputData ):
    """ input = { #group, heith, width, #channel } """
    if len( inputData.shape ) != 4:
        sys.stderr.write( "Error: ReLU layer input data should be 4 dimmentional" )
        sys.exit( 1 )
    reslut = NP.zeros( inputData.shape, dtype=NP.float16 )
    ( numGroup, height, width, numChannel ) = inputData.shape
    for groupIter in range( numGroup ):
        for i in range( height ):
            for j in range( width ):
                for c in range( numChannel ):
                    result[ groupIter, i, j, c ] = inputData[groupIter, i, j, c] 
                    if result[groupIter, i, j, c] < 0:
                        result[groupIter, i, j, c] = 0
    return result


# ---------------------------------------------------------------------------------------------------------
#    Pooling
# ---------------------------------------------------------------------------------------------------------
def AlexNet_Pooling( inputData, windowShape, stepShape = ( 1, 1) ):
    """ Pooling operation in alexnet """

    inputHeight, inputWidth = inputData.shape
    winHeight, winWidth = windowShape.shape
    stepH, stepW = stepShape.shape
    if ((inputHeight - winHeight) % stepH != 0) or (( inputWidth - winWidth ) % stepW != 0 ):
        sys.stdout.write( "Warning: Pooling (input_size - win_size) not multiple of step!\n" ) 
        sys.stdout.write( "input=(%d, %d), window=(%d, %d), step=(%d, %d)\n"
                % ( inputHeight, inputWidth, winHeight, winWidth, stepH, stepW ) )

    resultHeight = (inputHeight - winHeight)/stepH
    resultWidth  = (inputWidth - winWidth)/stepW

    result = NP.zeros( (resultHeight, resultWidth) ).astype( NP.float16 )
    for i in range( 0, inputHeight, stepH ):
        for j in range( 0, inputWidth, stepW ):
            result[i, j] = inputData[i, j]
            for win_i in range( i, winHeight + i, 1 ):
                for win_j in range( j, winWidth + j, 1 ):
                    if inputData[ win_i, win_j ] > result[i, j]:
                        result[i, j] = inputData[win_i, win_j]
    return result


# ---------------------------------------------------------------------------------------------------------
#    Norm
# ---------------------------------------------------------------------------------------------------------
def AlexNet_Norm( inputData, k, alpha, beta, n ) :
    """ InputData: (g, x, y, c) """
    if len( inputData.shape ) != 4:
        sys.stderr.write( "Error: norm layer need to be 4 dimentional!\n" )
        sys.exit( 1 )
    
    ret = NP.zeros( inputData.shape )
    numGroup, height, width, numChannel = inputData.shape
    for g in range( numGroup ):
        for i in range( height ):
            for j in range( width ):
                for c in range( numChannel ):
                    left  = max( 0, c - n//2 )
                    right = min( numChannel - 1, c + n//2 )
                    squareSum = 0
                    for iterC in range( left, right ):
                        squareSum = squareSum + inputData[g, i, j, iterC]*inputData[g, i, j, iterC]
                    ret[g, i, j, c] = inputData[g, i, j, c]/pow( k + alpha*squareSum, beta )
                
    return ret;
