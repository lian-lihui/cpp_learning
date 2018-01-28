sr_pool_one_window(
       .io_param .u8 win_h,
       .io_param .u8 win_w,
       .io_param .u8  output_h,
       .io_param .u8  output_w,
       .io_param .u8  logic_stride_h,
       .io_param .u8  logic_stride_w, 
       .io_param .u8  n_repeat
       .io_param .u32 ub_input_ptr,
       .io_param .u32 ub_rslt_ptr
                  )
{
    .u16 iter_win_h;
    .u16 iter_win_w;
    for( iter_win_h = 0, iter_win_h < win_h; iter_win_h++ ) {
        for( iter_win_w = 0; iter_win_w < win_w; iter_win_w++ ) {
            if ( iter_win_h == 0 && iter_win_w == 0 ) {
                // move element( 0, 0 ) to UB, with repeat effect
                //   src_addr     =  ub_input_ptr
                //   dest_addr    =  ub_rslt_ptr 
                //   num_burst    = output_w 
                //   contig_burst = 1 ( burst )  
                //   dest_gap     = 0 ( contigous in dest ub )
                ub_input_ptr1 += phy_stride_h;
                continue;
            }

            /* Do partial pooling by vector comparison */
            vmax.f16( ub_rslt_ptr, ub_rslt_ptr, ub_input_ptr,
                    1,              // result stride between blocks
                    1,              // Xm stride between blocks
                    logic_stride_w, // Xn stride between blocks
                    8,              // result stride between repeation
                    8,                  // Xm stride between repeation
                    8 * logic_stride_w, // Xn stride between repeation
                    n_repeat - 1        // repeat times
                    MASK = All 1's )
        }
    }
}

sr_pooling_tier(
    .param .b64 ub_input,
    .param .b64 ub_rslt,
    .param .u8  win_h,
    .param .u8  win_w,
    .param .u16 input_h,
    .param .u16 input_w,
    .param .u16 output_h,
    .param .u16 output_w,
    .param .u8  logic_stride_h,
    .param .u8  logic_stride_w,
    .param .u8  pad_top,
    .param .u8  pad_bot,
    .param .u8  pad_l,
    .param .u8  pad_r,
    .param .u32 phy_stride_h,
    .param .u32 phy_stride_w )
{
    /* calculate repeat times */
    .u32 n_iter_row = output_h;
    .u32 iter_row = 0;
    .u32 ub_input_ptr = ub_input;
    .u32 ub_rslt_ptr = ub_rslt;
    for ( iter_row = 0; iter_row < n_iter_row; iter_row ++ ) {
        if ( iter_row == n_iter_row - 1 ) {
            /* do the last padding */
            if ( iter_row == n_iter_row - 1 ) {
  
            }

        } else {
            /* do the regular padding */
            .u32 n_repeat = floor_div( output_w, 8 );
            .u32 iter_win_h;
            .u32 iter_win_w;
            .u32 ub_input_ptr1 = ub_inputr_ptr0;
            MASK = 0XFFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF
            sr_pool_one_window( win_h, win_w, output_h, output_w, logic_stride_h, logic_stride_w,
                                n_repeat-1, ub_input_ptr, ub_rslt_ptr )
            /*
            for( iter_win_h = 0, iter_win_h < win_h; iter_win_h++ ) {
                for( iter_win_w = 0; iter_win_w < win_w; iter_win_w++ ) {
                     if ( iter_win_h == 0 && iter_win_w == 0 ) {
                         // move element( 0, 0 ) to UB, with repeat effect
                         //   src_addr     =  ub_input_ptr
                         //   dest_addr    =  ub_rslt_ptr 
                         //   num_burst    = output_w 
                         //   contig_burst = 1 ( burst )  
                         //   dest_gap     = 0 ( contigous in dest ub )
                         ub_input_ptr1 += phy_stride_h;
                         continue;
                     }
                    
                     /* Do partial pooling by vector comparison */
                     vmax.f16( ub_rslt_ptr, ub_rslt_ptr, ub_input_ptr,
                                1,              // result stride between blocks
                                1,              // Xm stride between blocks
                                logic_stride_w, // Xn stride between blocks
                                8,              // result stride between repeation
                                8,                  // Xm stride between repeation
                                8 * logic_stride_w, // Xn stride between repeation
                                n_repeat - 1        // repeat times
                                MASK = All 1's )
                }
            }


        } */

        /* blocks including the last column */ 
        ub_input_ptr += phy_stride_w * (n_repeat -1);
        ub_rslt_ptr  += 8 * (n_repeat - 1);
        MASK = 0XFFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF
        for( iter_win_w = 0; iter_win_w < win_w; iter_win_w++ ) {
             if ( iter_win_h == 0 && iter_win_w == 0 ) {
                 if ( iter_win_h == 0 && iter_win_w == 0 ) {
                     // move element( 0, 0 ) to UB, with repeat effect
                     //   src_addr     =  ub_input_ptr
                     //   dest_addr    =  ub_rslt_ptr 
                     //   num_burst    = output_w 
                     //   contig_burst = 1 ( burst )  
                     //   dest_gap     = 0 ( contigous in dest ub )
                     ub_input_ptr1 += phy_stride_h;
                     continue;
                 }
             }
        }
    } // for each pooling row
}
