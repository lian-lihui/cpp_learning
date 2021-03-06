
import numpy as NP
import singleLayer

def conv1( ):
    """ conv1: input  { c=4,  x=228, y=228 }
               weight { x=11, y=11, c=4, k=48, g=2 } """

    # Generate binary input
    inputArr = NP.random.rand( 228, 228, 4 ).astype( NP.float16 )
    fInput = open( "AlexNet/data/conv1_input.data", "wb" )
    fInput.write( inputArr.tobytes( ) )
    fInput.close( )

    # Generate binary weight 
    weight = NP.random.rand( 2, 48, 11, 11, 4 ).astype( NP.float16 )
    fWeight = open( "AlexNet/data/conv1_weight.data", "wb" )
    fWeight.write( weight.tobytes( ) )
    fWeight.close( )

    # Do convolution
    singleLayer.AlexNet_conv1( inputArr[NP.newaxis, :, :, :], weight, padding=False, crossGroup=True )

def relu1( ):
    """ relu1: input { g=2, x=55, y=55, c=48 } """
    inputArr = NP.random.rand( 2, 55, 55, 48 ).astype( NP.float16 )
    inputArr = inputArr - 0.5
    fInput = open( "AlexNet/data/relu1.data", "wb" )
    fInput.write( inputArr.tobytes( ) )
    fInput.close( )

def norm1( ):
    """ norm1: input { g=2, x=55, y=55, c=48 }"""
    inputArr = NP.random.rand( 2, 55, 55, 48 ).astype( NP.float16 )
    fInput = open( "AlexNet/data/norm1.data", "wb" )
    fInput.write( inputArr.tobytes( ) )
    fInput.close( )

def pool1( ):
    """ pool1: input { g=2, x=55, y=55, c=48 } """
    inputArr = NP.random.rand( 2, 55, 55, 48 ).astype( NP.float16 )
    fInput = open( "AlexNet/data/pool1.data", "wb" )
    fInput.write( inputArr.tobytes( ) )
    fInput.close( )

def conv2( ):
    """ input{ g=2, x=27, y=27, c=48 }
        weight{ g=2, k=128, x=5, y=5, c=48 }"""
    inputArr = NP.random.rand( 2, 27, 27, 48 ).astype( NP.float16 )
    fInput = open( "AlexNet/data/conv2_input.data", "wb" )
    fInput.write( inputArr.tobytes( ) )
    fInput.close( )

    weight = NP.random.rand( 2, 128, 5, 5, 48 ).astype( NP.float16 )
    fWeight = open( "AlexNet/data/conv2_weight.data", "wb" )
    fWeight.write( weight.tobytes( ) )
    fWeight.close( )

def relu2( ):
    """ input{ g=2, x=27, y=27, c=128 } """
    inputArr = NP.random.rand( 2, 27, 27, 128 ).astype( NP.float16 )
    inputArr = inputArr - 0.5
    fInput = open( "AlexNet/data/relu2.data", "wb" )
    fInput.write( inputArr.tobytes( ) )
    fInput.close( )

def norm2( ):
    """ input{ g=2, x=27, y=27, c=128 } """
    inputArr = NP.random.rand( 2, 27, 27, 128 ).astype( NP.float16 )
    fInput = open( "AlexNet/data/norm2.data", "wb" )
    fInput.write( inputArr.tobytes( ) )
    fInput.close( )

def pool2( ):
    """ intput{ g=2, c=128, x=27, y=27 }"""
    inputArr = NP.random.rand( 2, 27, 27 ,128 ).astype( NP.float16 )
    fInput = open( "AlexNet/data/pool2.data", "wb" )
    fInput.write( inputArr.tobytes( ) )
    fInput.close( )

def conv3( ):
    """ input{ g=2, x=13, y=13, c=128 },
        weight{ g=2x2, k=192, x=3, y=3, c=128 } """
    inputArr = NP.random.rand( 2, 13, 13, 128 ).astype( NP.float16 )
    fInput = open( "AlexNet/data/conv3_input.data", "wb" )
    fInput.write( inputArr.tobytes( ) )
    fInput.close( )

    weight = NP.random.rand( 4, 192, 3, 3, 128 ).astype( NP.float16 )
    fWeight = open( "AlexNet/data/conv3_weight.data", "wb" )
    fWeight.write( weight.tobytes( ) )
    fWeight.close( )


def relu3( ):
    """ input{ g=2, x=13, y=13, c=192 } """
    inputArr = NP.random.rand( 2, 13, 13, 192 ).astype( NP.float16 )
    inputArr = inputArr - 0.5
    fInput = open( "AlexNet/data/relu3.data", "wb" )
    fInput.write( inputArr.tobytes( ) )
    fInput.close( )

def conv4( ):
    """ input{ g=2, x=13, y=13, c=192 }"""
    inputArr = NP.random.rand( 2, 13, 13, 192 ).astype( NP.float16 )
    fInput = open( "AlexNet/data/conv4.data", "wb" )
    fInput.write( inputArr.tobytes( ) )
    fInput.close( )

def relu4( ):
    """ input{ g=2, x=13, y=13, c=192 } """
    inputArr = NP.random.rand( 2, 13, 13, 192 ).astype( NP.float16 )
    inputArr = inpuArr - 0.5
    fInput = open( "AlexNet/data/relu4.data", "wb" )
    fInput.write( inputArr.tobytes( ) )
    fInput.close( )
   
def conv5( ):
    """ input{ g=2, x=13, y=13, c=192 }
        weight{ g=2, k=192, x=3, y=3, c=192 )"""
    inputArr = NP.random.rand( 2, 13, 13, 192 ).astype( NP.float16 )
    fInput = open( "AlexNet/data/conv5_input.data", "wb" )
    fInput.write( inputArr.tobytes( ) )
    fInput.close( )

    weight = NP.random.rand( 2, 192, 3, 3, 192 ).astype( NP.float16 )
    fWeight = open( "AlexNet/data/conv5_weight.data", "wb" )
    fWeight.write( weight.tobytes( ) )
    fWeight.close( )

def relu5( ):
    """ input { g=2, x=13, y=13, c=128 } """
    inputArr = NP.random.rand( 2, 13, 13, 128 ).astype( NP.float16 )
    inputArr = inputArr - 0.5
    fInput = open( "AlexNet/data/relu5.data", "wb" )
    fInput.write( inputArr.tobytes( ) )
    fInput.close( )

def pool5( ):
    """ input{ g=2, x=13, y=13, c=128 }"""
    inputArr = NP.random.rand( 2, 13, 13, 128 ).astype( NP.float16 )
    fInput = open( "AlexNet/data/pool5.data", "wb" )
    fInput.write( inputArr.tobytes( ) )
    fInput.close( )

def fc6( ):
    """ Input{9216}
        weight{ 9216, 4096 } """
    inputArr = NP.random.rand( 9216 ).astype( NP.float16 )
    fInput = open( "AlexNet/data/fc6_input.data", "wb" )
    fInput.write( inputArr.tobytes( ) )
    fInput.close( )

    weightOrig = NP.random.rand( 9216, 4096 ).astype( NP.float16 )
    weight = NP.zeros( (9216, 4096), dtype = NP.float16 )
    for block_i in range( 0, 9216/256, 256 ):
        for block_j in range( 0, 4096/128, 128):
            for tile_iter in range( 16 ):
                for i in range ( tile_iter, 256, 16 ):
                    for j in range( 128 ):
                        prim_row = block_i*256 + i
                        prim_col = block_j*128 + j
                        transformed_row = (prim_row*4096 + prim_col)/4096
                        transformed_col = (prim_row*4096 + prim_col)%4096
                        weight[transformed_row][transformed_row] = weightOrig[prim_row][prim_col]
    fWeight = open( "AlexNet/data/fc6_weight.data", "wb" )
    fWeight.write( weight.tobytes( ) )
    fWeight.close( )

def fc7( ):
    """ input{ 4096 }
        weight{ 4096, 4096 } """
    inputArr = NP.random.rand( 4096 ).astype( NP.float16 )
    fInput = open( "AlexNet/data/fc7_input.data", "wb" )
    fInput.write( inputArr.tobytes( ) )
    fInput.close( )

    weightOrig = NP.random.rand( 4096, 4096 ).astype( NP.float16 )
    weight = NP.zeros( (4096, 4096), dtype = NP.float16 )
    for block_i in range( 0 ,4096/256, 256 ):
        for block_j in range( 0, 4096/128, 128):
            for tile_iter in range( 16 ):
                for i in range ( tile_iter, 256, 16 ):
                    for j in range( 128 ):
                        prim_row = block_i*256 + i
                        prim_col = block_j*128 + j
                        transformed_row = (prim_row*4096 + prim_col)/4096
                        transformed_col = (prim_row*4096 + prim_col)%4096
                        weight[transformed_row][transformed_row] = weightOrig[prim_row][prim_col]
    fWeight = open( "AlexNet/data/fc7_weight.data", "wb" )
    fWeight.write( weight.tobytes( ) )
    fWeight.close( )

def fc8( ):
    """ input { 4096 },
        weight{ 4096, 1000 } """
    inputArr = NP.random.rand( 4096 ).astype( NP.float16 )
    fInput = open( "AlexNet/data/fc8_input.data", "wb" )
    fInput.write( inputArr.tobytes( ) )
    fInput.close( )

def AlexNet( ):
    conv1( )
    relu1( )
    norm1( )
    pool2( )

    conv2( )
    relu2( )
    norm2( )
    pool2( )

    conv3( )
    relu3( )
    conv4( )
    relu4( )
    conv5( )
    relu5( )
    pool5( )

    fc6( )
    fc7( )

if __name__ == "__main__":
    AlexNet( )
